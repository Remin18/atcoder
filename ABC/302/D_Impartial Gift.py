def solve():
    N, M, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()

    ans = -1
    for a in A:
        left, right = 0, M - 1
        if abs(a - B[right]) <= D:
            ans = max(ans, a + B[right])
            continue

        while right - left > 1:
            mid = (left + right) // 2

            if B[mid] <= a + D:
                left = mid
            else:
                right = mid

        if abs(a - B[left]) <= D:
            ans = max(ans, a + B[left])

    print(ans)

if __name__ == '__main__':
    solve()
