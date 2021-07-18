# Chess board is 8x8
TAM = 8

# Set a max for comparison since sys is not allowed
MAX = 100*100

# Chess board representation
board = [[0 for i in range(TAM)] for j in range(TAM)]

# Has a position been visited and how many steps it took to reach it
board_status = [[[False, MAX] for i in range(TAM)] for j in range(TAM)]


def init(tam):
    c = 0
    for i in range(tam):
        for j in range(tam):
            board[i][j] = c
            c = c+1

# Generate all possible destinations from a source position
def movements(src):
    dst = []
    src_i = src[0]
    src_j = src[1]

    # Go upwards
    dst.append([src_i - 2, src_j + 1])
    dst.append([src_i - 2, src_j - 1])

    # Go down
    dst.append([src_i + 2, src_j + 1])
    dst.append([src_i + 2, src_j - 1])

    # Go left
    dst.append([src_i + 1, src_j - 2])
    dst.append([src_i - 1, src_j - 2])

    # Go right
    dst.append([src_i + 1, src_j + 2])
    dst.append([src_i - 1, src_j + 2])

    valid_dst = []
    for mov in dst:
        if (mov[0] >= 0 and mov[1] >= 0) and (mov[0] < TAM and mov[1] < TAM):
            valid_dst.append(mov)

    return valid_dst


def update_status(movs, steps):
    for mov in movs:
        if board_status[mov[0]][mov[1]][0]:
            if board_status[mov[0]][mov[1]][1] > steps:
                board_status[mov[0]][mov[1]][1] = steps

        else:
            board_status[mov[0]][mov[1]][0] = True
            board_status[mov[0]][mov[1]][1] = steps


def arrival_check(destinations, final_dst):
    res = False

    for dst in destinations:
        if board[dst[0]][dst[1]] == final_dst:
            res = True

    return res


def recursion(dest, movs, steps, min_steps):
    if arrival_check(movs, dest):
        return steps

    else:
        steps = steps + 1
        update_status(movs, steps)
        for mov in movs:
            new_movs = movements(mov)
            for new_mov in new_movs:
                if not board_status[new_mov[0]][new_mov[1]][0] or \
                        board_status[new_mov[0]][new_mov[1]][1] > steps:
                    res = recursion(dest, new_movs, steps, min_steps)
                    if res and res < min_steps:
                        min_steps = res

    return min_steps


def solution(src, dest):
    init(TAM)
    steps = 0
    mov_ini = [int(src/TAM), src % TAM]
    return recursion(dest, [mov_ini], steps, MAX)


if __name__ == '__main__':
    print(solution(62, 20))
