def linear_search(lst, target):
    """Return index of target in list, or -1 if not found. O(n) time."""
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1


# Example
myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15
print(linear_search(myArray, myTarget))  # 7
