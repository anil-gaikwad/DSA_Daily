



def binary_search(lst, target):
    left = 0 
    right = len(lst) -1


    while left < right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        
        if lst[mid] < target:
            left +=1
        else:
            right +=1
    
    return -1


myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15
print(binary_search(myArray, myTarget))


