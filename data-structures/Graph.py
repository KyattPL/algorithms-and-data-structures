class Graph:
    def __init__(self):
        self.path = []
        self.vertices = []
        self.neighbors = []

    def add_node(self, number, neighbors):
        self.vertices.append(number)
        self.neighbors.append(neighbors)
        self.path.append(0)

    # 0 - white, 1 - grey, 2 - black
    def BFS(self, start):
        color = [0] * len(self.vertices)
        distance = [0] * len(self.vertices)
        queue = []
        for vert in self.vertices:
            if vert != start:
                color[vert] = 0
                self.path[vert] = None
        color[start] = 1
        distance[start] = 0
        self.path[start] = None
        queue.append(start)
        while len(queue) != 0:
            u = queue.pop(0)
            for vert in self.neighbors[u]:
                if color[vert] == 0:
                    color[vert] = 1
                    distance[vert] = distance[u] + 1
                    self.path[vert] = u
                    queue.append(vert)
            color[u] = 2

    def DFS(self, start):
        visited = [False] * (len(self.vertices))
        self.DFS_move(start, visited)

    def DFS_move(self, vert, visited):
        visited[vert] = True
        print(vert, end=' ')

        for adj in self.neighbors[vert]:
            if visited[adj] == False:
                self.DFS_move(adj, visited)

    def print_path(self, start, end):
        if start == end:
            print(start)
        elif self.path[end] == None:
            print("Path from " + str(start) + " to " +
                  str(end) + " doesn't exist!")
        else:
            self.print_path(start, self.path[end])
            print(str(end) + " ")


if __name__ == "__main__":
    g = Graph()
    g.add_node(0, [1])
    g.add_node(1, [0, 2, 3])
    g.add_node(2, [1, 3, 5])
    g.add_node(3, [1, 2, 4])
    g.add_node(4, [3, 5])
    g.add_node(5, [2, 4, 6])
    g.add_node(6, [5])
    g.BFS(0)
    g.print_path(0, 6)
    g.DFS(4)
