from itertools import combinations
N = int(input())
ices = list([list(map(int, input().split())) for _ in range(N)])
ices = sorted(ices, key=lambda x: x[1], reverse=True)

target_ices = []
ice_dict = {}
for ice in ices:
    is_add = False
    if ice[0] in ice_dict:
        if len(ice_dict[ice[0]]) <= 1:
            ice_dict[ice[0]].append(ice[1])
            is_add = True

    else:
        ice_dict[ice[0]] = [ice[1]]
        is_add = True

    if is_add:
        target_ices.append(ice)

    if (len(ice_dict.keys()) >= 2):
        break

maxval = 0
for a, b in combinations(target_ices, 2):
    if a[0] != b[0]:
        val = a[1] + b[1]
    else:
        min_val = min(a[1], b[1])
        max_val = max(a[1], b[1])
        val = max_val + int(min_val / 2)
    maxval = max(maxval, val)

print(maxval)
