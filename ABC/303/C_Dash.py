def solve():
    N, M, H, K = map(int, input().split())
    S = input()
    items = {"_".join(input().split()): 1 for _ in range(M)}

    pos = [0, 0]
    for s in S:
        if s == 'R':
            pos[0] += 1
        elif s == 'L':
            pos[0] -= 1
        elif s == 'U':
            pos[1] += 1
        elif s == 'D':
            pos[1] -= 1

        H -= 1
        if H < 0:
            print("No")
            return

        if H < K:
            key = "_".join(map(str, pos))
            if key in items:
                if items[key] == 1:
                    H = K
                    items[key] = 0

    print("Yes")

if __name__ == '__main__':
    solve()
