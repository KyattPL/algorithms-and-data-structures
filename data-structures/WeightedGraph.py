from DisjointSet import ForestOfTrees


def take_weight(elem):
    return elem[2]


class WeightedGraph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, number):
        self.vertices.append(number)

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def kruskal(self):
        ans = []
        forest = ForestOfTrees()
        for vert in self.vertices:
            forest.make_set(vert)
        edges = sorted(self.edges, key=take_weight)
        print(edges)
        for edge in edges:
            if forest.find_set(edge[0]) != forest.find_set(edge[1]):
                ans.append((edge[0], edge[1]))
                forest.union(edge[0], edge[1])
        return ans

    def edge_exists(self, start, vertex):
        for edge in self.edges:
            if start == edge[0] and vertex == edge[1]:
                return (True, edge[2])
        return (False, -1)

    def minimum_dist(self, distance, visited):
        minimum = float("inf")
        min_index = -1
        for vert in self.vertices:
            if distance[vert] < minimum and vert not in visited:
                minimum = distance[vert]
                min_index = vert

        return min_index

    def get_weight(self, start, end):
        for edge in self.edges:
            if start == edge[0] and end == edge[1]:
                return edge[2]
        return float("inf")

    def dijkstra_single_source(self, start):
        visited = []
        distance = [0] * len(self.vertices)
        for vertex in self.vertices:
            (exists, weight) = self.edge_exists(start, vertex)
            if vertex != start and exists:
                distance[vertex] = weight
            else:
                distance[vertex] = float("inf")
        while len(visited) != len(self.vertices):
            u = self.minimum_dist(distance, visited)
            visited.append(u)
            for vert in self.vertices:
                if vert not in visited:
                    distance[vert] = min(
                        distance[vert], distance[u] + self.get_weight(u, vert))

        print(distance)


if __name__ == "__main__":
    g = WeightedGraph()
    for i in range(7):
        g.add_vertex(i)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 6)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 5, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(4, 5, 5)
    g.add_edge(5, 6, 3)
    print(g.kruskal())
    g.dijkstra_single_source(0)
