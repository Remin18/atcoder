def solve():
    N, M = map(int, input().split())
    prints = [list(map(int, input().split())) for _ in range(M)]

    p = {}
    for i in list(range(1, N+1)):
        p[i] = set()

    for i in range(M):
        for j in range(N):
            if j != 0:
                p[prints[i][j]].add(prints[i][j-1])

            if j != N - 1:
                p[prints[i][j]].add(prints[i][j+1])

    ans = set()
    members = set(range(1, N+1))
    for i, pset in p.items():
        if len(pset) == M - 1:
            continue

        for j in members - pset:
            if i == j:
                continue
            key = "_".join(map(str, sorted([i, j])))
            ans.add(key)

    print(len(ans))

if __name__ == '__main__':
    solve()
