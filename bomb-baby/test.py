from main import solution

def testsolution(x, y):
    return "impossible"


def new_generation(arr, objective):
    new_arr = []

    for generation in arr:
        new_arr.append([generation[0], generation[1] + generation[0]])
        new_arr.append([generation[0] + generation[1], generation[1]])

    return new_arr


def test(n):
    arr = [[1, 2]]
    for i in range(n - 1):
        arr = new_generation(arr, 10)

        for generated in arr:
            sol = solution(str(generated[0]), str(generated[1]))
            if (i+2) != int(sol):
                print("ERROR")
                break