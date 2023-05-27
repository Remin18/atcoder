def solve():
    N = int(input())
    S = input()
    T = input()

    for s, t in zip(S, T):
        if s == t:
            continue

        elif s == '1' or s == 'l':
            if t == '1' or t == 'l':
                continue

        elif s == '0' or s == 'o':
            if t == '0' or t == 'o':
                continue

        print("No")
        return

    print("Yes")

if __name__ == '__main__':
    solve()
