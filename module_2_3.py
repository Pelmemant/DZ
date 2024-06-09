L = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
N = 0
M = len(L)
while N <= M:
    if L[N] > 0:
        print(L[N])
    elif L[N] < 0:
        break
    N = N + 1
    continue
