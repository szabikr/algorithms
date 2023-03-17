def bubble_sort(l):
    for j in range(len(l)):
        swapped = False
        for i in range(len(l) - 1 - j):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
        if not swapped:
            break
    return l

if __name__ == "__main__":
    l = [56, 65, 74, 100, 99, 68, 86, 180, 90]
    sorted_l = bubble_sort(l)
    print(sorted_l)