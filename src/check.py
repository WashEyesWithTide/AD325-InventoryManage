def check_Restock(inv: list[int]) -> None:
    # solution: O(n) time, O(1) space
    n = len(inv)
    zeros = 0
    for i in range(n-1):
        if inv[i] == 0:
            if i + zeros + 1 < n:
                zeros += 1
            else:
                break
        if i + zeros + 1 == n:
            break
    if zeros == 0:
        return
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
    inv = [1, 2, 3, 0]
    check_Restock(inv)
    print(inv)