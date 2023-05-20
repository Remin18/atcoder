def solve():
    A, B = map(int, input().split())
    ans, a = divmod(A, B)
    if a != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    solve()
