# https://atcoder.jp/contests/abc304/tasks/abc304_a
def solve():
    N = int(input())
    ps = [input().split() for _ in range(N)]

    min_p = min(ps, key=lambda x: int(x[1]))
    idx = ps.index(min_p)

    for i in range(idx, N):
        print(ps[i][0])

    if idx > 0:
        for i in range(0, idx):
            print(ps[i][0])

if __name__ == '__main__':
    solve()
