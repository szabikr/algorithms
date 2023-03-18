"""
Find all peak elements in an array, together with the plateaus.
Marking the beginning of plateaus.

Return a list of pairs with the indexes and the values.
"""

def find_peaks(l: list[int]) -> list[tuple[int, int]]:
    indexes = []
    prob_peak = False
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            prob_peak = i
        elif l[i] < l[i-1] and prob_peak:
            indexes.append(prob_peak)
            prob_peak = False
    return [(i, l[i]) for i in indexes]

if __name__ == "__main__":
    l = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]
    print(find_peaks(l))