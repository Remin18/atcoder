def solve():
    a, b, c, x = map(int, [input() for _ in range(4)])

    count = 0
    for i in range(a + 1):
        total_i = i * 500
        if total_i == x:
            count += 1
            break

        if total_i > x:
            break

        for j in range(b + 1):
            total_j = j * 100
            if total_i + total_j == x:
                count += 1
                break

            if total_i + total_j > x:
                break

            for k in range(c + 1):
                total_k = k * 50
                if total_i + total_j + total_k == x:
                    count += 1
                    break

                if total_i + total_j + total_k > x:
                    break

    print(count)

if __name__ == '__main__':
    solve()
