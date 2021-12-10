class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}

        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)

            if current_vertex == end_vertex:
                return True
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()

                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                start.extend(next_vertices)

        return False


railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

railway.find_path('peel', 'ulfstead')
