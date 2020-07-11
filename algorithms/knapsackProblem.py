class Element:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def find_elem(i, x, weight, solution, val):
    if x > 0 and i == -1:
        return 0
    elif x < 0 and i == -1:
        return float("-inf")
    else:
        if x - weight >= 0:
            return max(solution[i-1][x], solution[i-1][x-weight] + val)
        elif x - weight == -1:
            return val
        else:
            return solution[i-1][x]


def read_solution(solution, elements):
    current_value = solution[-1][-1]
    taken_items = []
    for i in range(len(elements) - 1, -1, -1):
        current_item = solution[i]
        val = elements[i].value
        if current_value - val in current_item:
            current_value -= val
            taken_items.append(i)

    for item in taken_items:
        val = elements[item].value
        weight = elements[item].weight
        print("Element of weight: " + str(weight) + ", and value: " + str(val))


def knapsack_dynamic(elements, size):
    solution = []
    first_line = []

    for i in range(len(elements)):
        newLine = []
        for j in range(size):
            newLine.append(0)
        solution.append(newLine)

    for i in range(size):
        index = elements[0].weight - 1
        if index <= i:
            first_line.append(elements[0].value)
        else:
            first_line.append(0)

    solution[0] = first_line

    for i in range(1, len(elements)):
        weight = elements[i].weight
        val = elements[i].value
        for x in range(size):
            solution[i][x] = find_elem(i, x, weight, solution, val)

    read_solution(solution, elements)


if __name__ == "__main__":
    elements = []
    elements.append(Element(3, 5))
    elements.append(Element(10, 12))
    elements.append(Element(8, 10))
    elements.append(Element(6, 7))
    elements.append(Element(2, 1))
    elements.append(Element(9, 11))
    knapsack_dynamic(elements, 20)
