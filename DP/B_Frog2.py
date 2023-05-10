def solve():
    N, K = map(int, input().split(" "))
    steps = list(map(int, input().split(" ")))

    inf = float('inf')
    dp = [inf] * N
    dp[0] = 0
    dp[1] = abs(steps[1] - steps[0])

    for i in range(2, N):
        for j in range(1, K+1):
            if i-j >= 0:
                dp[i] = min(abs(steps[i] - steps[i-j]) + dp[i-j], dp[i])

    print(dp[N-1])

if __name__  == "__main__":
    solve()
