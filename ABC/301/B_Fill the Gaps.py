# https://atcoder.jp/contests/abc301/tasks/abc301_b
def solve():
    N = int(input())
    S = list(map(int, input().split(' ')))

    ans = [S[0]]

    for i in range(1, N):
        diff = abs(S[i-1] - S[i])
        if diff == 1:
            ans.append(S[i])
            continue

        if S[i] > S[i-1]:
            ans.extend(list(range(S[i-1]+1, S[i])))
        else:
            ans.extend(list(range(S[i-1], S[i]+1, -1)))
        ans.append(S[i])

    print(*ans)

if __name__ == '__main__':
    solve()
