import json

import numpy as np


def main(points):
    rectangles = []

    # Point = [y, x]
    for first in points:
        v_all_1 = points - first
        seconds = points[(points[:, 0] > first[0]) &
                         (points[:, 1] >= first[1])]

        for second in seconds:
            # Find perpendicular
            v_2_1 = second - first
            v_all_2 = points - second
            thirds = points[((v_all_2 * v_2_1).sum(axis=1) == 0) &
                            (points[:, 1] > second[1])]

            for third in thirds:
                v_3_2 = third - second
                v_all_3 = points - third
                fourth = points[((v_all_3 * v_3_2).sum(axis=1) == 0) &
                                ((v_all_1 * v_all_3).sum(axis=1) == 0) &
                                (points[:, 0] < third[0])].tolist()

                if fourth:
                    rectangles.append([first.tolist(), second.tolist(),
                                       third.tolist(), fourth[0]])

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
