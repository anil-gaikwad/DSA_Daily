
def binary_search(lst, target):
    """Return index of target in sorted list, or -1 if not found. O(log n) time."""
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example
myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15
print(binary_search(myArray, myTarget))  # 7
