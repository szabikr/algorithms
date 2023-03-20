"""
Find an element in an ordered list and return its index.
"""

from typing import Optional

def binary_search(array: list[int], item: int) -> Optional[int]:
    low = 0
    high = len(array) - 1
    while low <= high:
        pos = (low + high) // 2
        guess = array[pos]
        if guess == item:
            return pos
        if guess > item:
            high = pos - 1
        else:
            low = pos + 1
    return None

if __name__ == "__main__":
    array = [0, 12, 14, 15, 19, 20, 27, 28, 33, 35, 37, 38, 44, 61, 65, 67, 69, 82, 96, 99]
    print(binary_search(array, 44))
