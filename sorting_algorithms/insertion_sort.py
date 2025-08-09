

def insertion_sort(custom_list):
    n = len(custom_list)

    for i in range(1, n):
        value = custom_list[i]
        j = i - 1
        while j >=0 and value < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -=1
        
        custom_list[j+1] = value

    return custom_list



custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

in_sort = insertion_sort(custom_list)
print(in_sort)


def insertion_sort(custom_list):
    n = len(custom_list)

    for i in range(1,n):
        index = i
        curr_value = custom_list.pop(i)
        for j in range(i-1, -1, -1):
            if custom_list[j] > curr_value:
                index =j
        custom_list.insert(index, curr_value)

    return custom_list



custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

in_sort = insertion_sort(custom_list)
print(in_sort)


def insertion_sort(custom_list):
    n = len(custom_list)

    for i in range(1, n):
        value = custom_list[i]
        index = i 
        for j in range(i-1, -1, -1):
            if custom_list[j] > value:
                index = j
                custom_list[j+1] = custom_list[j]
            else:
                break
        custom_list[index] = value

    return custom_list



custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

in_sort = insertion_sort(custom_list)
print(in_sort)