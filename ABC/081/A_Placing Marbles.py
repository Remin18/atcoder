def solve():
    s = input()

    ball = 0
    for i in range(len(s)):
        if s[i] == '1':
            ball += 1

    print(ball)

if __name__ == '__main__':
    solve()
