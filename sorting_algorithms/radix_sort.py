

def radix_sort(custom_list):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    exp = 1
    max_val = max(custom_list)

    while max_val // exp > 0:
        while len(custom_list) > 0:
            val = custom_list.pop()
            radix_index = (val // exp) % 10
            radixArray[radix_index].append(val)
        
        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                custom_list.append(val)
            
        exp *=10
    

custom_list = [64, 34, 25, 12, 22, 11, 90, 5]

radix_sort(custom_list)
print(custom_list)
