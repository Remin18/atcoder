# https://atcoder.jp/contests/abc305/tasks/abc305_c
def solve():
    H, W = map(int, input().split())
    maps = [input() for _ in range(H)]

    min_idx = -1
    max_cookie = 0
    row_start, row_end = 0, 0
    for idx, row in enumerate(maps):
        cnt = row.count('#')
        if cnt == 0:
            continue

        max_cookie = max(cnt, max_cookie)
        if min_idx == -1:
            min_idx = idx
        elif cnt > 0 and max_cookie > cnt:
            min_idx = idx
            break

        tmp_start, tmp_end = -1, -1
        for j in range(len(row)):
            if row[j] != '#':
                continue

            if tmp_start == -1:
                tmp_start = j

            tmp_end = j

        row_start, row_end = tmp_start, tmp_end

    for idx, s in enumerate(maps[min_idx][row_start:row_end+1]):
        if s == '.':
            print(*[min_idx + 1, row_start + idx + 1])
            return

if __name__ == '__main__':
    solve()
