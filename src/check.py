def check_Restock(inv: list[int]) -> None:
    n = len(inv)
    i = 0
    while i < n:
        if inv[i] == 0:
            # Shift elements from the end down by one, dropping the last element.
            for j in range(n - 1, i + 1, -1):
                inv[j] = inv[j - 1]
            # Place the duplicate zero (only if there's a next slot).
            if i + 1 < n:
                inv[i + 1] = 0
            i += 2  # Skip over both zeros
        else:
            i += 1


def check_Restock_2(inv: list[int]) -> None:
    n = len(inv)
    zeros = 0
    for i in range(n):
        if inv[i] == 0:
            if i + zeros + 1 < n:
                zeros += 1
            else:
                break
        if i + zeros + 1 == n:
            break

    last = n - 1
    i = n - 1 - zeros
    while i >= 0:
        if inv[i] == 0:
            inv[last] = 0
            last -= 1
            if last >= 1:
                inv[last] = 0
                last -= 1
        else:
            inv[last] = inv[i]
            last -= 1
        i -= 1

if __name__ == "__main__":
    inv = [0, 0, 1, 2]
    check_Restock_2(inv)
    print(inv)