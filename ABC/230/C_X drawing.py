# 以下の入力でNG
# 1000000000000000000 999999999999999999 999999999999999999
# 999999999999999998 1000000000000000000 999999999999999998 1000000000000000000

def solve():
    N, A, B = map(int, input().split(' '))
    P, Q, R, S = map(int, input().split(' '))

    table = [['.'] * N for _ in range(N)]

    for k in range(max(1-A, 1-B), min(N-A, N-B) + 1):
        k -= 1
        if 0 > A+k or A+k >= N or 0 > B+k or B+k >= N:
            continue
        table[A+k][B+k] = '#'

    for k in range(max(1-A, B-N), min(N-A, B-1) + 1):
        if 0 > A+k-1 or A+k-1 >= N or 0 > B-k-1 or B-k-1 >= N:
            continue
        table[A+k-1][B-k-1] = '#'

    for i in range(P-1, Q):
        print(''.join(table[i][R-1:S]))

if __name__ == '__main__':
    solve()
