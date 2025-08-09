
## O(n^2)
def bubble_sort(custom_list):

    n = len(custom_list)
    for i  in range(n-1):
        for j in range(n-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]

    return custom_list


custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

b_sort = bubble_sort(custom_list)
print(b_sort)



## O(n)
def bubble_sort(custom_list):

    n = len(custom_list)
    for i  in range(n-1):
        swap = False
        for j in range(n-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
                swap = True
        if not swap:
            break
    return custom_list


custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

b_sort = bubble_sort(custom_list)
print(b_sort)