

def merge_sort(custom_list):
    if len(custom_list) <=1:
        return custom_list
    
    mid = len(custom_list) // 2
    
    lefthalf = custom_list[:mid]
    righthalf = custom_list[mid:]

    sortedleft = merge_sort(lefthalf)
    sortedright = merge_sort(righthalf)

    return merge(sortedleft, sortedright)

def merge(left, right):
    result = []
    i = 0
    j = 0 

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
        
    result.extend(left[i:])
    result.extend(right[j:])

    return result



custom_list = [3, 7, 6, -10, 15, 23.5, 55, -13]
m_sort = merge_sort(custom_list)
print(m_sort)