
def selection_sort(custom_list):

    n = len(custom_list)
    for i  in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if custom_list[j] < custom_list[min_index]:
                min_index = j
        min_val = custom_list.pop(min_index)
        custom_list.insert(i, min_val)

    return custom_list


custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

s_sort = selection_sort(custom_list)
print(s_sort)

# O(n^2)

def selection_sort(custom_list):

    n = len(custom_list)
    for i  in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if custom_list[j] < custom_list[min_index]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]

    return custom_list


custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

s_sort = selection_sort(custom_list)
print(s_sort)