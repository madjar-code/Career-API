import networkx as nx
from pyvis.network import Network
from graph.models import Node, Growth

# DATABASE_NAME = 'CN-Agro.db'

JOB_COLOR = 'green'
EDU_COLOR = 'yellow'
JOB_TYPE = 10
EDU_TYPE = 9


class GraphService2:

    def __init__(self) -> None:
        self.nx_graph = nx.Graph()
        self.create_graph()

    def create_graph(self) -> None:
        self.nx_graph = nx.DiGraph()
        nodes = Node.active_objects.all()

        type_color = {
            JOB_TYPE: JOB_COLOR,
            EDU_TYPE: EDU_COLOR
        }

        for node in nodes:
            node_label = f'[{node.id}] {node.name}'
            node_color = type_color[node.node_type]
            self.nx_graph.add_node(node.id, size=10, label=node_label, color=node_color)

        growths = Growth.active_objects.all()

        for growth in growths:
            self.nx_graph.add_edge(
                growth.start_node.id,
                growth.end_node.id,
                weight=3
            )

    def visualize_all(self):
        network = Network(height='900px', notebook=True, directed=True)
        network.from_nx(self.nx_graph)
        network.show('main_graph.html')

    def build_route_AB(self, node_id_1: int, node_id_2: int) -> str:
        result_subgraph = nx.DiGraph()

        nodes = nx.shortest_path(self.nx_graph, node_id_1, node_id_2)
        result_subgraph.add_nodes_from(nodes)
        list_of_node_ids = list(result_subgraph)
        for node_id in result_subgraph.nodes:
            result_subgraph.nodes[node_id]['label'] = self.nx_graph.nodes[node_id]['label']
            result_subgraph.nodes[node_id]['color'] = JOB_COLOR    # JOB_COLOR is 'green'

        for i in range(1, len(list_of_node_ids)):
            result_subgraph.add_edge(list_of_node_ids[i-1], list_of_node_ids[i])

        return 'OK', list_of_node_ids

    def build_route_A(self, node_id_1: int) -> str:
        """
        Career opportunities by profession
        """
        try:
            result_subgraph = nx.DiGraph()
            result_subgraph = nx.bfs_tree(self.nx_graph, node_id_1)

            for node_id in result_subgraph.nodes:
                result_subgraph.nodes[node_id]['label'] = self.nx_graph.nodes[node_id]['label']
        except:
            return 'Something went wrong'
        return 'OK'

    def build_route_B(self, node_id_2: int) -> str:
        """
        Career path to profession
        """
        try:
            #TODO: это надо вынести в отдельную функцию
            reverse_subgraph = nx.DiGraph()
            result_subgraph = nx.DiGraph()
            reverse_subgraph = nx.reverse(self.nx_graph)
            result_subgraph = nx.bfs_tree(reverse_subgraph, node_id_2)
            result_subgraph = nx.reverse(result_subgraph)

            for node_id in result_subgraph.nodes:
                result_subgraph.nodes[node_id]['label'] = self.nx_graph.nodes[node_id]['label']
        except:
            return 'Something went wrong'
        return 'OK'
