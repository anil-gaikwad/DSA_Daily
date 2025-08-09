

def counting_sort(custom_list):
    max_val = max(custom_list)
    count = [0] * (max_val + 1)

    while len(custom_list):
        num = custom_list.pop(0)
        count[num] += 1
    
    for i in range(len(count)):
        while count[i] > 0:
            custom_list.append(i)
            count[i] -=1
    return custom_list


custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

c_sort = counting_sort(custom_list)
print(c_sort)
