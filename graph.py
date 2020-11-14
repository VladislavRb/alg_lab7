class Vertex:
    def __init__(self, v_id: int):
        self.id = v_id
        self.incident_edges = []
        self.is_visited = False

    def __forms_cycle_method_without_cycle_status_cleansing(self, other):
        if self.id == other.id:
            return True

        available_edges = list(filter(
            lambda edge: not edge.must_be_visited and not edge.is_in_cycle, other.incident_edges))

        if not len(available_edges):
            return False

        for edge in available_edges:
            edge.is_in_cycle = True

        return True in [self.__forms_cycle_method_without_cycle_status_cleansing(next_vertex)
                        for next_vertex in list(map(lambda edge: edge.second_vertex(other), available_edges))]

    def forms_cycle_by_connection_with(self, other, edges_list: list):
        forms_cycle = self.__forms_cycle_method_without_cycle_status_cleansing(other)

        for edge in edges_list:
            edge.is_in_cycle = False

        return forms_cycle

    def __eq__(self, other):
        return self.id == other.id


class Edge:
    def __init__(self, start_vertex: Vertex, end_vertex: Vertex, weight: int):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight
        self.must_be_visited = True
        self.is_in_cycle = False

    def second_vertex(self, first_vertex: Vertex):
        return self.end_vertex if self.start_vertex == first_vertex else self.start_vertex

    def __str__(self):
        return str(self.start_vertex.id) + "-" + str(self.end_vertex.id) + "   "


class CompleteGraph:
    def __init__(self, weight_matrix: list):
        self.n = len(weight_matrix)
        self.vertices = [Vertex(i) for i in range(self.n)]
        self.edges = []

        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                edge = Edge(self.vertices[i], self.vertices[j], weight_matrix[i][j])

                self.vertices[i].incident_edges.append(edge)
                self.vertices[j].incident_edges.append(edge)

                self.edges.append(edge)

    def __prim_possible_next_edges(self):
        possible_edges_list = []

        for visited_vertex in list(filter(lambda vertex: vertex.is_visited, self.vertices)):
            possible_edges_list.extend(
                list(filter(
                    lambda edge: not visited_vertex.forms_cycle_by_connection_with(edge.second_vertex(visited_vertex),
                                                                                   self.edges),
                    visited_vertex.incident_edges)))

        return possible_edges_list

    def __kruskal_possible_next_edges(self):
        unvisited_edges = list(filter(lambda edge: edge.must_be_visited, self.edges))

        return list(filter(
            lambda edge: not edge.start_vertex.forms_cycle_by_connection_with(edge.end_vertex, self.edges),
            unvisited_edges))

    def prim(self):
        spanning_tree_edges_list = []

        min_edge = min(self.edges, key=lambda edge: edge.weight)
        current_vertex = min_edge.start_vertex

        while False in list(map(lambda vertex: vertex.is_visited, self.vertices)):
            current_vertex.is_visited = True

            possible_next_edges = self.__prim_possible_next_edges()

            if len(possible_next_edges):
                next_edge = min(possible_next_edges, key=lambda edge: edge.weight)
                next_edge.must_be_visited = False
                spanning_tree_edges_list.append(next_edge)

                current_vertex = next_edge.end_vertex if next_edge.start_vertex.is_visited else next_edge.start_vertex

        for v in self.vertices:
            v.is_visited = False

        for e in self.edges:
            e.must_be_visited = True

        return spanning_tree_edges_list

    def kruskal(self):
        spanning_tree_edges_list = []

        while True:
            possible_next_edges = self.__kruskal_possible_next_edges()

            if len(possible_next_edges):
                next_edge = min(possible_next_edges, key=lambda edge: edge.weight)
                next_edge.must_be_visited = False
                spanning_tree_edges_list.append(next_edge)
            else:
                break

        for e in self.edges:
            e.must_be_visited = True

        return spanning_tree_edges_list
