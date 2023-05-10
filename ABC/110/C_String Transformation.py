def solve():
    A = input()
    B = input()

    change_dict_a = {}
    change_dict_b = {}

    is_change = True
    for i in range(len(A)):
        if A[i] not in change_dict_a:
            change_dict_a[A[i]] = B[i]
        else:
            if change_dict_a[A[i]] != B[i]:
                is_change = False
                break

        if B[i] not in change_dict_b:
            change_dict_b[B[i]] = A[i]
        else:
            if change_dict_b[B[i]] != A[i]:
                is_change = False
                break

    print("Yes" if is_change else "No")

if __name__ == '__main__':
    solve()
