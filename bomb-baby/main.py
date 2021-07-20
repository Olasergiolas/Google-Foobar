import copy


def equals(a, b):
    a_reverse = copy.deepcopy(a)
    a_reverse.reverse()

    res = True if a == b or a_reverse == b else False
    return res


def solution(x, y):
    steps = 0
    current = [int(x), int(y)]

    '''if (current[0] % 2 == 0) and (current[1] % 2 == 0):
        return "impossible"'''

    while current != [1, 1]:
        steps = steps + 1
        op_1 = [current[0] - current[1], current[1]]
        op_2 = [current[0], current[1] - current[0]]
        current = op_1

        if (op_1[0] <= 1 or op_1[1] <= 1) and (op_2[0] >= 1 and op_2[1] >= 1):
            current = op_2

        '''elif (op_1[0] <= 1 or op_1[1] <= 1) and (op_2[0] <= 1 or op_2[1] <= 1):
            return "impossible"'''

    return str(steps)


if __name__ == '__main__':
    a = 4
    b = 7
    print(solution(str(a), str(b)))