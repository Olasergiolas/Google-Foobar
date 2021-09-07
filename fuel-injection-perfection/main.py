# TODO Prettify the code so it doesn't suck
# TODO Come up with a better algorithm

def solution(n):
    int_n = int(n)
    steps = 0

    while int_n != 1:
        while not int_n % 2:
            steps = steps + 1
            int_n = int_n / 2
            #print(int_n)

        else:
            if int_n != 1:
                steps = steps + 1
                superior = int_n + 1
                inferior = int_n - 1

                if superior == 2 or inferior == 2:
                    int_n = 2
                    continue

                sup_par = (superior/2) % 2
                inf_par = (inferior/2) % 2

                if not sup_par and inf_par:
                    eleccion = superior

                elif not sup_par and not inf_par:
                    eleccion = min(superior, inferior)

                else:
                    eleccion = inferior

                #print eleccion
                int_n = eleccion

    return steps
    # print steps


if __name__ == '__main__':
    print solution('15')
