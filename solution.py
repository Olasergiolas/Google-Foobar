import math


def solution(area):
    sol = []
    area_left = int(area)

    while area_left > 0:
        side_float = math.sqrt(area_left)
        side_int = int(side_float)
        panel_area = side_int ** 2
        sol.append(panel_area)
        area_left -= panel_area

    return sol
