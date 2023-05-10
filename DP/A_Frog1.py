def solve():
    N = int(input())
    steps = list(map(int, input().split(" ")))

    inf = float('inf')
    dp = [inf] * N
    dp[0] = 0
    dp[1] = abs(steps[1] - steps[0])

    for i in range(2, N):
        dp[i] = min(abs(steps[i] - steps[i-1]) + dp[i-1], abs(steps[i] - steps[i-2]) + dp[i-2])
    print(dp[N-1])

if __name__  == "__main__":
    solve()
