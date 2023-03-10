from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import\
    api_view
from drf_yasg.utils import swagger_auto_schema
from graph.models import Node
from graph.services.graph_service import GraphService2
from graph.api.serializers import SimpleNodeSerializer


graph_service = GraphService2()


@swagger_auto_schema(method='GET', operation_id='all_nodes')
@api_view(['GET'])
def get_all_nodes(request: Request) -> Response:
    """
    Endpoint for getting all nodes from database.
    """
    nodes = Node.active_objects.all()
    serializer = SimpleNodeSerializer(nodes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='GET', operation_id='graph_page')
@api_view(['GET'])
def get_graph_page(request: Request) -> Response:
    """
    Create html-page with graph
    """
    global graph_service
    graph_service.visualize_all()
    return Response('Complete!', status=status.HTTP_200_OK)


@swagger_auto_schema(method='GET', operation_id='route_between')
@api_view(['GET'])
def get_builded_route_AB(request: Request,
                         prof_edu_id_1: int,
                         prof_edu_id_2: int) -> Response:
    """
    Endpoint for getting builded route between
    profession (or education) with prof_edu_id_1 and profession (or education) with
    prof_edu_id_2
    """
    global graph_service
    data = graph_service.build_route_AB(prof_edu_id_1, prof_edu_id_2)
    return Response({'message': str(data)}, status.HTTP_200_OK)


@swagger_auto_schema(method='GET', operation_id='route_by')
@api_view(['GET'])
def get_builded_route_A(request: Request,
                         prof_edu_id_1: int) -> Response:
    """
    Endpoint for getting career opportunities
    by profession (or education) with prof_edu_id_1
    """
    global graph_service
    data = graph_service.build_route_A(prof_edu_id_1)
    return Response({'message': str(data)}, status.HTTP_200_OK)


@swagger_auto_schema(method='GET', operation_id='route_to')
@api_view(['GET'])
def get_builded_route_B(request: Request,
                         prof_edu_id_2: int) -> Response:
    """
    Endpoint for getting career path
    to profession (or education) with prof_edu_id_2
    """
    global graph_service
    data = graph_service.build_route_B(prof_edu_id_2)
    return Response({'message': str(data)}, status.HTTP_200_OK)
