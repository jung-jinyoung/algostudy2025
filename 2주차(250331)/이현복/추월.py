def func(n, repeat):
    ans = 0
    mul = 1
    for i in range(repeat):
        ans += (mul * n)
        mul *= 10
    return ans


def solution(N, number):
    if N == number:
        return 1

    arr = [set() for _ in range(9)]
    for i in range(1, 9):
        tmp = func(N, i)
        if tmp == number:
            return i
        else:
            arr[i].add(tmp)
        for j in range(1, i):
            for A in arr[i - j]:
                for B in arr[j]:
                    if A + B == number:
                        return i
                    else:
                        arr[i].add(A + B)
                    if A * B == number:
                        return i
                    else:
                        arr[i].add(A * B)
                    if A - B == number:
                        return i
                    else:
                        arr[i].add(A - B)

                    if B:
                        if A // B == number:
                            return i
                        else:
                            arr[i].add(A // B)
    return -1