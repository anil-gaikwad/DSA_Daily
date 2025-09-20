# Input: List = [1, 2, 3, [1, [6, 7, 5, [23, 7, 3], 19], 22]]
# Expected Output: List = [1, 2, 3, 1, 6, 7, 5, 23, 7, 3, 19, 22]

# 1. Recursive Solution
def flatten1(lst):
    res = []

    for i in lst:
        if isinstance(i,list):
            res.extend(flatten1(i))
        else:
            res.append(i)
    return res


# 2. Iterative (stack-based)
def flatten2(lst):
    res = []
    stack = lst[::-1]

    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(curr[::-1])
        else:
            res.append(curr)
    return res

# 3. Generator version
def flatten3(lst):
    for i in lst:
        if isinstance(i, list):
            yield from flatten3(i)
        else:
            yield i

# 4.Two Pointer
def flatten4(lst):

    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            lst[i:i+1] = lst[i]
        else:
            i += 1
    return lst

    

lst = [1, 2, 3, [1, [6, 7, 5, [23, 7, 3], 19], 22]]
print(flatten1(lst))
print(flatten2(lst))
print(list(flatten3(lst)))
print(flatten4(lst))

