def quick_sort(l: list[int]) -> list[int]:
    if len(l) < 2:
        return l
    pivot = l[0]
    less = [i for i in l[1:] if i <= pivot]
    greater = [i for i in l[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    l = [56, 65, 74, 100, 99, 68, 86, 180, 90]
    print(quick_sort(l))

