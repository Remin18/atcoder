import math

def solve():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()

    d_pre = x[1] - x[0]
    ans = d_pre
    for i in range(1, N):
        d_now = x[i+1] - x[i]
        ans = min(math.gcd(d_now, d_pre), ans)
        d_pre = d_now

    print(ans)

if __name__ == '__main__':
    solve()
