import random


def compareVer(v1, v2):
    # v1 < v2 by default
    res = True
    equals = True

    v1 = v1.split(".")
    v1[:] = [int(x) for x in v1]
    v2 = v2.split(".")
    v2[:] = [int(x) for x in v2]

    for i in range(min(len(v1), len(v2))):
        if v1[i] != v2[i]:
            equals = False

        if v1[i] > v2[i]:
            res = False
            break

        elif v1[i] < v2[i]:
            break

    if equals and len(v1) > len(v2):
        res = False

    return res


def quicksort(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index] = arr[high]
        arr[high] = pivot
        continuar = True

        while continuar:
            itemFromLeft = high
            itemFromRight = low
            for i in range(low, high+1):
                #if arr[i] > pivot:
                if not compareVer(arr[i], pivot):
                    itemFromLeft = i
                    break

            for i in range(high-1, low-1, -1):
                #if arr[i] < pivot:
                if compareVer(arr[i], pivot):
                    itemFromRight = i
                    break

            if itemFromLeft < itemFromRight:
                aux = arr[itemFromLeft]
                arr[itemFromLeft] = arr[itemFromRight]
                arr[itemFromRight] = aux

            else:
                continuar = False
                aux = arr[itemFromLeft]
                arr[itemFromLeft] = pivot
                arr[high] = aux

        arr = quicksort(arr, low, itemFromLeft - 1)
        arr = quicksort(arr, itemFromLeft + 1, high)

    return arr


def solution(l):
    return quicksort(l, 0, len(l)-1)


if __name__ == '__main__':
    arr = ["1.11", "1.2", "2", "0.1", "1.2.1", "2.0.0", "1.1.1"]
    print(solution(arr))