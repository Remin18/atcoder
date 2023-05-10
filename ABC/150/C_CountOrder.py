import sys
sys.setrecursionlimit(10**6)

def solve():
    N = int(input())
    P = list(map(int, input().split(" ")))
    Q = list(map(int, input().split(" ")))

    all_list = permutations(list(range(1, N + 1)))
    p_idx = -1
    q_idx = -1
    for idx, numset in enumerate(all_list):
        if P == numset:
            p_idx = idx + 1
        if Q == numset:
            q_idx = idx + 1

        if p_idx >= 0 and q_idx >= 0:
            break

    print(abs(p_idx - q_idx))

def permutations(target_list) -> list[list]:
    if len(target_list) <= 1:
        return [target_list]

    results = []
    for idx, val in enumerate(target_list):
        rest = permutations(target_list[:idx] + target_list[idx+1:])
        for param in rest:
            results.append([val] + param)

    return results

if __name__ == '__main__':
    solve()
