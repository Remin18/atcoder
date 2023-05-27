def solve():
    X, Y, Z = map(int, input().split())
    S = input()
 
    inf = float('inf')
    dp = [[inf] * len(S) for _ in range(2)]
 
    if S[0] == 'a':
        dp[0][0] = X
        dp[1][0] = Z + Y
    else:
        dp[0][0] = Y
        dp[1][0] = Z + X
 
    for i in range(1, len(S)):
        if S[i] == 'a':
            dp[0][i] = min(dp[0][i-1] + X, dp[1][i-1] + X + Z)
            dp[1][i] = min(dp[1][i-1] + Y, dp[0][i-1] + Y + Z)
 
        else:
            dp[0][i] = min(dp[0][i-1] + Y, dp[1][i-1] + Y + Z)
            dp[1][i] = min(dp[1][i-1] + X, dp[0][i-1] + X + Z)
 
    print(min(dp[0][-1], dp[1][-1]))
 
if __name__ == '__main__':
    solve()
