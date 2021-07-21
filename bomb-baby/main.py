import copy

# Check if two configurations of bombs are the same
def equals(a, b):
    a_reverse = copy.deepcopy(a)
    a_reverse.reverse()

    # It takes the same n of steps to get to [2,1] or [1,2]
    res = True if a == b or a_reverse == b else False
    return res

# Go end to root in the replication "tree"
def solution(x, y):
    steps = 0
    current = [int(x), int(y)]

    while current != [1, 1]:
        # For some cases like [1,4]
        if equals(current, [0, 1]):
            return str(steps-1)

        elif current[0] == 0 or current[1] == 0:
            return "impossible"

        a = int(current[0]/current[1])
        b = int(current[1]/current[0])

        if a > 0:
            current = [current[0] - current[1] * a, current[1]]
            steps = steps + a

        elif b > 0:
            current = [current[0], current[1] - current[0] * b]
            steps = steps + b

    return str(steps)


if __name__ == '__main__':
    a = 2
    b = 5
    print(solution(str(a), str(b)))