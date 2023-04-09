"""
Alogrihm complexity: O(n^2)
Sort a list of elements using the Selection Sort technique.

Find the index of the smallest element and move it to the new list.
"""

def find_min(l: list[int]) -> int:
    min, min_index = l[0], 0
    for i in range(1, len(l)):
        if l[i] < min:
            min, min_index = l[i], i
    return min_index

def selection_sort(l: list[int]) -> list[int]:
    result = []
    for _ in range(len(l)):
        min = find_min(l)
        result.append(l.pop(min))
    return result

def selection_sort_2(l: list[int]) -> list[int]:
    return [l.pop(find_min(l)) 
            for _ in range(len(l))]

if __name__ == "__main__":
    l = [56, 65, 74, 100, 99, 68, 86, 180, 90]
    print(l)
    print(selection_sort_2(l))