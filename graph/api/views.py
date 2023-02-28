from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import\
    api_view
from drf_yasg.utils import swagger_auto_schema
from graph.services.graph_service import GraphService


graph_service = GraphService()

@swagger_auto_schema(method='GET', operation_id='route_between')
@api_view(['GET'])
def get_builded_route_AB(request: Request,
                         prof_id_1: int,
                         prof_id_2: int) -> Response:
    """
    Endpoint for getting builded route between
    profession with prof_id_1 and profession with
    prof_id_2
    """
    global graph_service
    data = graph_service.build_route_AB(prof_id_1, prof_id_2)
    return Response({'message': str(data)}, status.HTTP_200_OK)


@swagger_auto_schema(method='GET', operation_id='route_by')
@api_view(['GET'])
def get_builded_route_A(request: Request,
                         prof_id_1: int) -> Response:
    """
    Endpoint for getting career opportunities
    by profession with prof_id_1
    """
    global graph_service
    data = graph_service.build_route_A(prof_id_1)
    return Response({'message': str(data)}, status.HTTP_200_OK)


@swagger_auto_schema(method='GET', operation_id='route_to')
@api_view(['GET'])
def get_builded_route_B(request: Request,
                         prof_id_2: int) -> Response:
    """
    Endpoint for getting career path
    to profession with prof_id_2
    """
    global graph_service
    data = graph_service.build_route_B(prof_id_2)
    return Response({'message': str(data)}, status.HTTP_200_OK)
