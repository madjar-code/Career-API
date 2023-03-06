import sqlite3
import networkx as nx

DATABASE_NAME = 'CN-Agro.db'

JOB_COLOR = 'green'
EDU_COLOR = 'yellow'
JOB_TYPE = 10
EDU_TYPE = 9


class GraphService:

    def __init__(self) -> None:
        connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = connection.cursor()
        self.nx_graph = nx.Graph()
        self.create_graph()

    def create_graph(self) -> None:
        self.nx_graph = nx.DiGraph()

        self.cursor.execute("SELECT * FROM professions")
        professions = self.cursor.fetchall()

        type_color = {
            JOB_TYPE: JOB_COLOR,
            EDU_TYPE: EDU_COLOR
        }

        for profession in professions:
            prof_id, prof_name, prof_type, _ = profession
            node_label = f'[{prof_id}] {prof_name}'
            node_color = type_color[prof_type]
            self.nx_graph.add_node(prof_id, size=15, label=node_label, color=node_color)

        self.cursor.execute("SELECT * FROM growths")
        growths = self.cursor.fetchall()

        for growth in growths:
            prof_id_1, prof_id_2, counter = growth[1], growth[2], growth[4]
            self.nx_graph.add_edge(prof_id_1, prof_id_2, weight=counter)

    def build_route_AB(self, prof_id_1: int, prof_id_2: int) -> str:
        result_subgraph = nx.DiGraph()

        try:
            nodes = nx.shortest_path(self.nx_graph, prof_id_1, prof_id_2)
            result_subgraph.add_nodes_from(nodes)

            for node_id in result_subgraph.nodes:
                result_subgraph.nodes[node_id]['label'] = self.nx_graph.nodes[node_id]['label']
                result_subgraph.nodes[node_id]['color'] = JOB_COLOR    # JOB_COLOR is 'green'

            prof_id_list = list(result_subgraph)
            for i in range(1, len(prof_id_list)):
                result_subgraph.add_edge(prof_id_list[i-1], prof_id_list[i])

        except nx.NetworkXNoPath:
            return 'No path'

        except nx.NodeNotFound:
            return 'None of the nodes'

        return 'OK'

    def build_route_A(self, prof_id_1: int) -> str:
        """
        Career opportunities by profession
        """
        try:
            result_subgraph = nx.DiGraph()
            result_subgraph = nx.bfs_tree(self.nx_graph, prof_id_1)

            for node_id in result_subgraph.nodes:
                result_subgraph.nodes[node_id]['label'] = self.nx_graph.nodes[node_id]['label']
        except:
            return 'Something went wrong'
        return 'OK'

    def build_route_B(self, prof_id_2: int) -> str:
        """
        Career path to profession
        """
        try:
            #TODO: это надо вынести в отдельную функцию
            reverse_subgraph = nx.DiGraph()
            result_subgraph = nx.DiGraph()
            reverse_subgraph = nx.reverse(self.nx_graph)
            result_subgraph = nx.bfs_tree(reverse_subgraph, prof_id_2)
            result_subgraph = nx.reverse(result_subgraph)

            for node_id in result_subgraph.nodes:
                result_subgraph.nodes[node_id]['label'] = self.nx_graph.nodes[node_id]['label']
        except:
            return 'Something went wrong'
        return 'OK'