# https://atcoder.jp/contests/abc141/tasks/abc141_d
import heapq
def solve():
    N, M = map(int, input().split(' '))
    items = list(map(lambda x: int(x) * -1, input().split(' ')))
    heapq.heapify(items)
    for _ in range(M):
        value = heapq.heappop(items) * -1
        heapq.heappush(items, value // 2 * -1)
    print(sum(items) * -1)

if __name__ == '__main__':
    solve()
