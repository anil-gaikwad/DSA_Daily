

def linear_search(lst, target):
    
    n = len(lst)

    for i in range(n):
        if lst[i] == target:
            return i
    
    return -1


myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15
print(linear_search(myArray, myTarget))