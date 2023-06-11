# https://atcoder.jp/contests/abc305/tasks/abc305_a
def solve():
    N = int(input())
    if N == 100:
        print(N)
        return

    if N == 0:
        print(N)
        return

    if N % 5 == 0:
        print(N)
        return

    num = int(str(N)[-1])
    if num <= 2:
        print(int(str(N)[:-1] + '0'))
    elif num > 2 and num <= 7:
        print(int(str(N)[:-1] + '5'))
    else:
        print(str(int(str(N)[:-1]) + 1) + '0')

if __name__ == '__main__':
    solve()
