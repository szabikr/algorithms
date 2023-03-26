"""
Sort a list of elements using the Selection Sort technique.

Find the index of the smallest element and move it to the new list.
"""

def find_min(l: list[int]) -> int:
    min = l[0]
    min_index = 0
    for i in range(1, len(l)):
        if l[i] < min:
            min = l[i]
            min_index = i
    return min_index

def selection_sort(l: list[int]) -> list[int]:
    result = []
    while l:
        result.append(l.pop(find_min(l)))
    return result

if __name__ == "__main__":
    l = [56, 65, 74, 100, 99, 68, 86, 180, 90]
    print(l)
    print(selection_sort(l))