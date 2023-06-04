# https://atcoder.jp/contests/abc304/tasks/abc304_b
def solve():
    N = int(input())

    ans = 0
    if N <= 10 ** 3 - 1:
        ans = N // 1 * 1

    elif N <= 10 ** 4 - 1:
        ans = N // 10 * 10

    elif N <= 10 ** 5 - 1:
        ans = N // 100 * 100

    elif N <= 10 ** 6 - 1:
        ans = N // 1000 * 1000

    elif N <= 10 ** 7 - 1:
        ans = N // 10000 * 10000

    elif N <= 10 ** 8 - 1:
        ans = N // 100000 * 100000

    elif N <= 10 ** 9 - 1:
        ans = N // 1000000 * 1000000

    print(ans)

if __name__ == '__main__':
    solve()
