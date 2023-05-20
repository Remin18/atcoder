from collections import deque

def solve():
    H, W = map(int, input().split())
    strs = [input() for _ in range(H)]

    moves = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    search_str = 'snuke'

    ans = list()
    for i in range(H):
        for j in range(W):
            if strs[i][j] != 's':
                continue

            for add_k, add_l in moves:
                que = deque()
                que.append((i, j, 1))
                ans = [(i+1, j+1)]

                while que:
                    k, l, idx = que.pop()

                    if k+add_k < 0 or k+add_k >= H or l+add_l < 0 or l+add_l >= W:
                        continue

                    if strs[k+add_k][l+add_l] != search_str[idx]:
                        continue

                    ans.append((k+add_k+1, l+add_l+1))
                    if len(ans) >= len(search_str):
                        for answer in ans:
                            print(*answer)
                        return

                    que.append((k+add_k, l+add_l, idx+1))

if __name__ == '__main__':
    solve()
