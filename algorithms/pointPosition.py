# Given three points on a plane, determine the position of the third
# point relative to p->q vector.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def position(p, q, r):
    first = p.x * q.y * 1
    second = q.x * r.y * 1
    third = r.x * p.y * 1
    part1 = first + second + third

    fourth = 1 * q.y * r.x
    fifth = 1 * r.y * p.x
    sixth = 1 * p.y * q.x
    part2 = fourth + fifth + sixth

    result = part1 - part2
    if result > 0:
        return 2
    elif result < 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    p = Point(5, 4)
    q = Point(3, 2)
    r = Point(6, 7)
    outcome = position(p, q, r)
    if outcome == 2:
        print("Point r is on the left side of pq vector")
    elif outcome == 1:
        print("Point r is on the right side of the pq vector")
    else:
        print("Point r is on the same line as pq vector")
