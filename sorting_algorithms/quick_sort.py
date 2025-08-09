
def partition(cusom_list, low, high):
    pivot = custom_list[high]
    print(cusom_list, pivot)
    i = low - 1

    for j in range(low, high):
        if cusom_list[j] <= pivot:
            i += 1
            cusom_list[i], cusom_list[j] = cusom_list[j], cusom_list[i]
    
    cusom_list[i+1], cusom_list[high] = cusom_list[high], cusom_list[i+1]
    return i + 1



def quick_sort(cusom_list, low=0, high=None):

    if high is None:
        high = len(cusom_list) - 1

    if low < high:
        pivot_index = partition(cusom_list, low, high)
        quick_sort(cusom_list, low, pivot_index-1)
        quick_sort(cusom_list,pivot_index+1, high)


custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

quick_sort(custom_list)
print(custom_list)

