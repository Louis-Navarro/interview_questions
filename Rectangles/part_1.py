import json

import numpy as np


def main(points):
    rectangles = []

    # Point = [y, x]
    for first in points:
        first = first.tolist()
        under = points[(points[:, 0] > first[0]) &
                       (points[:, 1] == first[1])]

        for second in under:
            second = second.tolist()
            right = points[(points[:, 1] > second[1]) &
                           (points[:, 0] == second[0])]

            for third in right:
                third = third.tolist()
                fourth = points[(points[:, 0] == first[0]) &
                                (points[:, 1] == third[1])].tolist()

                if fourth:
                    rectangles.append([first, second, third, fourth[0]])

    return len(rectangles)


if __name__ == '__main__':
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    data = np.array(data)

    if '.' in data:
        points = np.argwhere(data == '.')

    else:
        points = data

    rects = main(points)
    print(rects)
