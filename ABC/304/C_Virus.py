# https://atcoder.jp/contests/abc304/tasks/abc304_c
from collections import deque
import math

def solve():
    N, D = map(int, input().split())
    ps = [tuple(map(int, input().split())) for _ in range(N)]

    sicks = set()
    sicks.add(ps[0])

    que = deque()
    que.append(ps[0])

    def in_area(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2) <= D

    while que:
        p = que.popleft()

        for target in ps:
            if target in sicks:
                continue

            if not in_area(p, target):
                continue

            sicks.add(target)
            que.append(target)

    for p in ps:
        if p in sicks:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()
