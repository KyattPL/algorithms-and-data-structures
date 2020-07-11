from math import atan2, sqrt
from pointPosition import position


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


lowest_point = None


def angle(point):
    return atan2(point.y - lowest_point.y, point.x - lowest_point.x)


def distance(point):
    return sqrt((point.x - lowest_point.x)**2 + (point.y - lowest_point.y)**2)


def find_lowest(points):
    temp_low = points[0]
    minimum = float("inf")
    for p in points:
        if p.y < minimum:
            temp_low = p
            minimum = p.y
        elif p.y == minimum and p.x < temp_low.x:
            temp_low = p
    global lowest_point
    lowest_point = temp_low


def graham(points):
    points = sorted(points, key=lambda x: (angle(x), distance(x)))
    stack = []
    stack.append(points[0])
    stack.append(points[1])
    stack.append(points[2])
    for i in range(3, len(points)):
        while position(stack[-1], stack[-2], points[i]) == 2:
            stack.pop()
        stack.append(points[i])
    return stack


if __name__ == "__main__":
    points = []
    p1 = Point(3, 8)
    p2 = Point(1, 4)
    p3 = Point(2, 5)
    p4 = Point(7, 2)
    p5 = Point(3, 2)
    p6 = Point(5, 4)
    points.append(p1)
    points.append(p2)
    points.append(p3)
    points.append(p4)
    points.append(p5)
    points.append(p6)
    find_lowest(points)
    hull = graham(points)
    for point in hull:
        print("Point x: " + str(point.x) + ", y: " + str(point.y))
