from itertools import permutations

def solve():
    N, M = map(int, input().split())
    strs = [input() for _ in range(N)]
    strs.sort()

    def is_same(a, b):
        diff = 0
        for cur, bef in zip(a, b):
            if cur != bef:
                diff += 1
            if diff >= 2:
                return False
        return True

    result = False
    for s_list in permutations(strs):
        for i in range(1, len(s_list)):
            if i >= N:
                break

            if not is_same(s_list[i], s_list[i-1]):
                break
        else:
            result = True

        if result:
            break

    print("Yes" if result else "No")

if __name__ == '__main__':
    solve()
