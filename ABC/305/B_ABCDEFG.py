# https://atcoder.jp/contests/abc305/tasks/abc305_b
def solve():
    P, Q = input().split()
    dist = [3, 1, 4, 1, 5, 9]
    dist_dict = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
    }

    p_idx = dist_dict[P]
    q_idx = dist_dict[Q]
    p, q = sorted([p_idx, q_idx])

    ans = 0
    for i in range(p, q):
        ans += dist[i]

    print(ans)

if __name__ == '__main__':
    solve()
