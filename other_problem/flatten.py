######################  FLATTEN NESTED LIST  #########################
# Input:  [1, 2, 3, [1, [6, 7, 5, [23, 7, 3], 19], 22]]
# Output: [1, 2, 3, 1, 6, 7, 5, 23, 7, 3, 19, 22]

######################  1. Recursive Solution ######################
def flatten_recursive(lst):
    """
    Flatten a nested list recursively.
    """
    res = []
    for i in lst:
        if isinstance(i, list):
            res.extend(flatten_recursive(i))
        else:
            res.append(i)
    return res


######################  2. Iterative (Stack-based) ##################
def flatten_iterative(lst):
    """
    Flatten a nested list using a stack (iterative).
    """
    res = []
    stack = lst[::-1]
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(curr[::-1])
        else:
            res.append(curr)
    return res


######################  3. Generator Version #######################
def flatten_generator(lst):
    """
    Flatten a nested list using a generator.
    """
    for i in lst:
        if isinstance(i, list):
            yield from flatten_generator(i)
        else:
            yield i


######################  4. Two-Pointer / In-place ##################
def flatten_inplace(lst):
    """
    Flatten a nested list in-place using slicing.
    """
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            lst[i:i+1] = lst[i]  # replace nested list with its elements
        else:
            i += 1
    return lst


######################  DEMO ######################
if __name__ == "__main__":
    nested_list = [1, 2, 3, [1, [6, 7, 5, [23, 7, 3], 19], 22]]

    print("Recursive Flatten:")
    print(flatten_recursive(nested_list.copy()))

    print("\nIterative Flatten:")
    print(flatten_iterative(nested_list.copy()))

    print("\nGenerator Flatten:")
    print(list(flatten_generator(nested_list.copy())))

    print("\nIn-place Flatten:")
    print(flatten_inplace(nested_list.copy()))
