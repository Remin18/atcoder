# https://atcoder.jp/contests/abc301/editorial/6339
from collections import defaultdict
import string

def solve():
    S = input()
    T = input()

    ok_list = ['a', 't', 'c', 'o', 'd', 'e', 'r']
    s_cnt = defaultdict(int)
    t_cnt = defaultdict(int)

    for char in S: s_cnt[char] += 1
    for char in T: t_cnt[char] += 1

    at_total = s_cnt['@'] + t_cnt['@']
    is_ok = True
    diff = 0
    for char in string.ascii_lowercase:
        if s_cnt[char] == t_cnt[char] or char in ok_list:
            pass
        else:
            is_ok = False
            break

        diff += abs(s_cnt[char] - t_cnt[char])

    if is_ok and at_total >= diff:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()
