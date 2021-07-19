import copy


def equals(a, b):
    a_reverse = copy.deepcopy(a)
    a_reverse.reverse()

    res = True if a == b or a_reverse == b else False
    return res


def new_generation(arr, objective):
    new_arr = []

    for generation in arr:
        p_1 = [generation[0], generation[1] + generation[0]]
        p_2 = [generation[0] + generation[1], generation[1]]

        if equals(p_1, objective) or equals(p_2, objective):
            new_arr = 1
            break

        if p_1[0] + p_1[1] <= objective[0] + objective[1]:
            new_arr.append(p_1)

        if p_2[0] + p_2[1] <= objective[0] + objective[1]:
            new_arr.append(p_2)

    return new_arr


def solution(x, y):
    objective = [int(x), int(y)]
    continuar = True
    arr = [[1, 2]]

    if objective == [1, 1]:
        steps = 0
        continuar = False

    elif equals([1, 2], objective):
        steps = 1
        continuar = False

    else:
        steps = 2

    while continuar:
        arr = new_generation(arr, objective)
        if arr == 1:
            continuar = False

        elif len(arr) == 0:
            return "impossible"

        else:
            steps = steps + 1

    return str(steps)


if __name__ == '__main__':
    '''arr = [[1,2]]
    steps = 2
    continuar = True

    while continuar:
        arr = new_generation(arr, [5,3])
        if arr == -1 or len(arr) == 0:
            continuar = False

        else:
            steps = steps + 1

        print(arr)

    print(steps)'''

    sol = solution('2', '1')
    print(sol)