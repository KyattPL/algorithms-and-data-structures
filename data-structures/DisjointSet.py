class ForestOfTrees:
    def __init__(self):
        self.sets = []
        self.ranks = []

    def make_set(self, x):
        self.sets.append(x)
        self.ranks.append(x)

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if self.ranks[x] > self.ranks[y]:
            self.sets[y] = x
        else:
            self.sets[x] = y
            if self.ranks[x] == self.ranks[y]:
                self.ranks[y] += 1

    def find_set(self, x):
        if x != self.sets[x]:
            self.sets[x] = self.find_set(self.sets[x])
        return self.sets[x]

    def print_tabs(self, how_many):
        for disjoint in range(how_many):
            while self.sets[disjoint] != disjoint:
                print(str(disjoint) + " -> ", end="")
                disjoint = self.sets[disjoint]
            print(disjoint)


if __name__ == "__main__":
    trees = ForestOfTrees()
    how_many_sets = 6
    for x in range(how_many_sets):
        trees.make_set(x)
    trees.union(0, 4)
    trees.union(1, 3)
    trees.union(1, 5)
    trees.print_tabs(how_many_sets)
