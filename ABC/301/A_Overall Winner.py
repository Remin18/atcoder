# https://atcoder.jp/contests/abc301/tasks/abc301_a
def solve():
    N = int(input())
    S = input()

    t_win = S.count('T')
    a_win = S.count('A')

    t_temp = 0
    a_temp = 0
    win = ''
    if t_win == a_win:
        for win in S:
            if win == 'T':
                t_temp += 1
            else:
                a_temp += 1

            if t_win == t_temp or t_win == a_temp:
                break
        win = 'T' if t_temp > a_temp else 'A'
    else:
        win = 'T' if t_win > a_win else 'A'

    print (win)

if __name__ == '__main__':
    solve()
