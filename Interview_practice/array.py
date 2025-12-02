########################## 1. Binary Search ########################## 

# Q1. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

# Approach: Binary search by dividing search space in half.
# Time: O(log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
nums = [-1,0,3,5,9,12]
target = 9
print(binary_search(nums, target))  # Output: 4


########################## 2. Find the Duplicate Number ########################## 

# Q2. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Approach: Floyd's Tortoise and Hare (Cycle Detection)
# Time: O(n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def find_duplicate(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare

nums = [1,3,4,2,2]
print(find_duplicate(nums))  # Output: 2


########################## 3. Search Insert Position ########################## 

# Q3. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example:
# Input: nums = [1,2,3,4,6]  , target = 5
# Output: 4

# Approach: Binary search
# Time: O(log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = [1,2,3,4,6]
target = 5
print(search_insert_position(nums, target))  # Output: 4


########################## 4. Sort Colors ########################## 

# Q4. Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same 
# color are adjacent, with the colors in the order red, white, and blue. 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# You must solve this problem without using the library's sort function.

# Example:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Approach: Dutch National Flag algorithm
# Time: O(n), Space: O(1)
#--------------------------- Solution --------------------------------# 
def sort_colors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

nums = [2,0,2,1,1,0]
print(sort_colors(nums))  # Output: [0,0,1,1,2,2]


########################## 5. Find First and Last Position ########################## 

# Q5. Find First and Last Position

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position 
# of a given target value. If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Time: O(log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def find_first_last(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound
    return [find_bound(True), find_bound(False)]

nums = [5,7,7,8,8,10]
target = 8
print(find_first_last(nums, target))  # Output: [3,4]


########################## 6. Length of Last Word ########################## 

# Q6. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example:
# Input: s = "Hello World"
# Output: 5

# Approach: iterate from end or split string.
# Time: O(n), Space: O(1) or O(n) if split used
#--------------------------- Solution --------------------------------# 

def length_of_last_word(s):
    
    words = s.split()
    return len(words[-1])

s = "Hello World"
print(length_of_last_word(s))

def length_of_last_word(s):
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length

s = "Hello World"
print(length_of_last_word(s))  # Output: 5


########################## 7. Set Matrix Zeroes ########################## 

# Q7. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Approach: record rows/cols to zero and update matrix
# Time: O(m*n), Space: O(m+n)
#--------------------------- Solution --------------------------------# 

def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rows_to_zero, cols_to_zero = set(), set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    for i in range(rows):
        for j in range(cols):
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j] = 0
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zeroes(matrix))  # Output: [[1,0,1],[0,0,0],[1,0,1]]


########################## 8. Pascal's Triangle ########################## 

# Q8. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly

# Example:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Approach: build each row based on previous row
# Time: O(numRows^2), Space: O(numRows^2)
#--------------------------- Solution --------------------------------# 

def pascal_triangle(num):
    if num == 0:
        return []
    if num == 1:
        return [[1]]
    
    final_result = [[1], [1, 1]]
    for i in range(2, num):
        existing_data = final_result[i-1]
        new_row = [1]
        for j in range(1, len(existing_data)):
            new_row.append(existing_data[j-1] + existing_data[j])
        new_row.append(1)
        final_result.append(new_row)
    
    return final_result

numRows = 5
print(pascal_triangle(numRows))

def pascal_triangle(numRows):
    if numRows == 0: return []
    result = [[1]]
    for i in range(1, numRows):
        prev = result[-1]
        row = [1] + [prev[j-1]+prev[j] for j in range(1,len(prev))] + [1]
        result.append(row)
    return result

numRows = 5
print(pascal_triangle(numRows))  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


########################## 9. Single Element in Sorted Array ########################## 

# Q9. Single Element in Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once. Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Example:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Approach: Binary search using index parity
# Time: O(log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def single_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left)//2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid+1]:
            left = mid + 2
        else:
            right = mid
    return nums[left]

nums = [1,1,2,3,3,4,4,8,8]
print(single_element(nums))  # Output: 2


########################## 10. Search a 2D Matrix ########################## 

# Q10. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:
# • Each row is sorted in non-decreasing order.
# • The first integer of each row is greater than the last integer of then previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Approach: Binary search treating matrix as 1D
# Time: O(log(m*n)), Space: O(1)
#--------------------------- Solution --------------------------------# 

def search_matrix(matrix, target):
    if not matrix or not matrix[0]: 
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n -1

    while left <= right:
        mid = (left+right)//2
        row, col = mid//n, mid%n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid -1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search_matrix(matrix, target))  # Output: True


########################## 11. Pow(x, n) ########################## 

# Q11. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Approach: Exponentiation by squaring
# Time: O(log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

print(my_pow(2.0, 10))  # Output: 1024.0


########################## 12. Peak Element in 2D ########################## 

# Q12. Find a Peak Element in 2D grid

# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the 
# left, right, top, and bottom. Given a 0-indexed m x n matrix mat where no two adjacent cells are equal,
# find any peak element mat[i][j] and return the length 2 array [i,j].
# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

# Example:
# Input: mat = [[1,4],[3,2]]
# Output: [0,1]


# Approach: Binary search column-wise
# Time: O(m log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def find_peak_grid(mat):
    rows, cols = len(mat), len(mat[0])
    left, right = 0, cols-1
    while left <= right:
        mid = (left + right)//2
        max_row = max(range(rows), key=lambda i: mat[i][mid])
        if mid > 0 and mat[max_row][mid] < mat[max_row][mid-1]:
            right = mid-1
        elif mid < cols-1 and mat[max_row][mid] < mat[max_row][mid+1]:
            left = mid+1
        else:
            return [max_row, mid]

mat = [[1,4],[3,2]]
print(find_peak_grid(mat))  # Output: [0,1]


########################## 13. Max Value of Equation ########################## 

# Q13. Max Value of Equation

# You are given an array points containing the coordinates of points on a 2D
# plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1<= i < j <= points.length. 
# You are also given an integer k.
# Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.
# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

# Example:
# Input: x = [[1,3],[2,0],[5,10],[6,-10]], k = 1, n = 1
# Output: 4

# Approach: Monotonic deque
# Time: O(n), Space: O(n)
#--------------------------- Solution --------------------------------# 

from collections import deque

def find_max_value_of_equation(points, k):
    res = float('-inf')
    dq = deque()
    for x, y in points:
        while dq and x - dq[0][1] > k:
            dq.popleft()
        if dq:
            res = max(res, y + x + dq[0][0])
        while dq and dq[-1][0] <= y - x:
            dq.pop()
        dq.append((y - x, x))
    return res

points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(find_max_value_of_equation(points, k))  # Output: 4


########################## 14. Jump Game ########################## 

# Q14. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array 
# represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

# Example:
# Input: nums = [2,3,1,1,4]
# Output: true

# Approach: Track farthest reachable index
# Time: O(n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def can_jump(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True

nums = [2,3,1,1,4]
print(can_jump(nums))  # Output: True


########################## 15. Two Sum ########################## 

# Q15. Two Sum

# Given an array of integers nums and an integer target. Find two
# distinct indices i and j such that the sum of nums[i] and nums[j] is equal to the target.

# Example:
# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]

# Approach: Hashmap
# Time: O(n), Space: O(n)
#--------------------------- Solution --------------------------------# 

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))  # Output: [0,1]


########################## 16. Contains Duplicate ########################## 

# Q16. Contains Duplicate

# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is distinct.

# Example:
# Input: nums = [1,2,3,1]
# Output: True

# Approach: Set
# Time: O(n), Space: O(n)
#--------------------------- Solution --------------------------------# 

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))  # Output: True


########################## 17. Best Time to Buy and Sell Stock ########################## 

# Q17. Max Profit from Stock Prices

# Given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Approach: Track min price and max profit
# Time: O(n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))  # Output: 5

########################## 18. Valid Parentheses ########################## 

# Q18. Valid Parentheses

# Determine if an input string containing only the characters '(', ')',
# '{', '}', '[', and ']' is valid. A string is considered valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Each close bracket has a corresponding open bracket of the same type

# Example:
# Input: s = "()[]{}"
# Output: True

# Approach: Stack
# Time: O(n), Space: O(n)
#--------------------------- Solution --------------------------------# 

def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

s = "()[]{}"
print(is_valid_parentheses(s))  # Output: True


########################## 19. Maximum Sum Subarray of Size K ########################## 

# Q19. Maximum Sum Subarray of Size K

# Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

# Example:
# Input: nums = [2,3,4,1,5], k = 2
# Output: 7

# Approach: Sliding window
# Time: O(n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

nums = [2,3,4,1,5]
k = 2
print(max_sum_subarray(nums, k))  # Output: 7


########################## 20. Product of Array Except Self ########################## 

# Q20. Product of Array Except Self

# Given an array of integers, return a new array where each element at index i of the 
# new array is the product of all the numbers in the original array except the one at I

# Example:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Approach: Prefix and suffix products
# Time: O(n), Space: O(1) extra (output not counted)
#--------------------------- Solution --------------------------------# 

def product_except_self(nums):
    n = len(nums)
    res = [1]*n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

nums = [1,2,3,4]
print(product_except_self(nums))  # Output: [24,12,8,6]

########################## 21. Triplet Sum to Zero ########################## 

# Q21. Three Sum

# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Approach: Sort + two pointers
# Time: O(n^2), Space: O(n)
#--------------------------- Solution --------------------------------# 

def three_sum(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            s = nums[i]+nums[left]+nums[right]
            if s==0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left<right and nums[left]==nums[left-1]:
                    left +=1
                while left<right and nums[right]==nums[right+1]:
                    right -=1
            elif s<0:
                left +=1
            else:
                right -=1
    return triplets

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))  # Output: [[-1,-1,2],[-1,0,1]]

########################## 22. Merge Intervals ########################## 

# Q22. Merge Intervals

# Given a list of intervals, merge all the overlapping intervals to
# produce a list that has only mutually exclusive intervals.

# Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# Approach: Sort + iterate
# Time: O(n log n), Space: O(n)
#--------------------------- Solution --------------------------------# 

def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for curr in intervals[1:]:
        if curr[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], curr[1])
        else:
            merged.append(curr)
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]

########################## 23. Group Anagrams ########################## 

# Q23. Group Anagrams

# Given a list of strings, the task is to group the anagrams together.
# An anagram is a word or phrase formed by rearranging the letters of another, such as "cinema", formed from "iceman".

# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [['eat','tea','ate'],['tan','nat'],['bat']]

# Approach: Sort letters and use hashmap
# Time: O(n*k log k), Space: O(n*k), n=#strings, k=avg length
#--------------------------- Solution --------------------------------# 

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))  # Output: [['eat','tea','ate'],['tan','nat'],['bat']]


########################## 24. Maximum Product Subarray ########################## 

# Q24. Maximum Product Subarray

# Given an integer array, find the contiguous subarray (at least one number in it) 
# that has the maximum product. Return this maximum product.

# Example:
# Input: nums = [2,3,-2,4]
# Output: 6

# Approach: Track min and max product
# Time: O(n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def max_product_subarray(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(num, max_prod*num)
        min_prod = min(num, min_prod*num)
        result = max(result, max_prod)
    return result

nums = [2,3,-2,4]
print(max_product_subarray(nums))  # Output: 6


########################## 25. Search in Rotated Sorted Array ########################## 

# Q25. Search in Rotated Sorted Array

# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, 
# find if a given ‘key’ is present in it.
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. 
# You can assume that the given array does not have any duplicates.

# Example:
# Input: nums = [4,5,6,7,0,1,2], key = 0
# Output: 4

# Approach: Binary search considering rotated halves
# Time: O(log n), Space: O(1)
#--------------------------- Solution --------------------------------# 

def search_rotated(nums, key):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid]==key:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= key < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if nums[mid] < key <= nums[right]:
                left = mid+1
            else:
                right = mid-1
    return -1

nums = [4,5,6,7,0,1,2]
key = 0
print(search_rotated(nums, key))  # Output: 4