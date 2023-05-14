def solve():
    N = int(input())
    happies = [list(map(int, input().split(' '))) for _ in range(N)]

    dp = [[0] * 3 for _ in range(N)]
    dp[0] = happies[0]

    for i in range(1, N):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i-1][1] + happies[i][j], dp[i-1][2] + happies[i][j])
            elif j == 1:
                dp[i][j] = max(dp[i-1][0] + happies[i][j], dp[i-1][2] + happies[i][j])
            elif j == 2:
                dp[i][j] = max(dp[i-1][0] + happies[i][j], dp[i-1][1] + happies[i][j])

    print(dp[N-1])

if __name__ == '__main__':
    solve()
