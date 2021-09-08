def getStepsPowerOfTwo(pellets, steps):
    # A power of two only has one bit set, so let's flip every bit by substracting one and
    # perform an AND operation with itself to check if the result is 0
    if pellets & (pellets - 1) == 0:
        while pellets != 1:
            pellets >>= 1
            steps += 1

        return steps

    else:
        return -1


def solution(n):
    pellets = int(n)
    steps = 0

    # Get to 1 pellet
    while pellets != 1:
        steps_pot = getStepsPowerOfTwo(pellets, steps)
        if steps_pot != -1:
            return steps_pot

        # Always divide by 2 if even
        while not pellets % 2:
            steps += 1
            pellets /= 2

        # If not even let's decide whether to increase or reduce by one the n of pellets
        else:
            if pellets != 1:
                steps += 1
                sup = pellets + 1
                prev = pellets - 1

                # If one of the choices is two, always stick with that
                if sup == 2 or prev == 2:
                    pellets = 2
                    continue

                even_sup = (sup/2) % 2
                even_prev = (prev/2) % 2

                # Given that both choices will be even, stick with the one that gives
                # an even result after dividing by 2
                if not even_sup and even_prev:
                    choice = sup

                elif not even_sup and not even_prev:
                    choice = min(sup, prev)

                else:
                    choice = prev

                pellets = choice

    return steps


if __name__ == '__main__':
    print solution('15')
