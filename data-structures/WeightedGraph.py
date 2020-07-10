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
