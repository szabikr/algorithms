def sum_elements(l: list[int]) -> int:
    if len(l) == 0:
        return 0
    return l[0] + sum_elements(l[1:])

if __name__ == "__main__":
    l = [2, 4, 6]
    print(sum_elements(l))
