# https://atcoder.jp/contests/abc140/tasks/abc140_c

def solve():
    N = int(input())
    B = list(map(int, input().split(' ')))

    total = B[0] + B[-1]
    for i in range(1, N-1):
        total += min(B[i], B[i-1])
    print(total)

if __name__ == '__main__':
    solve()
