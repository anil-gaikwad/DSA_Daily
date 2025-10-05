
########################## 1. Binary Search ########################## 

# Q 1. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

#---------------------- Solution -----------------------------# 

def binary_search(nums, target):
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1 


nums = [-1,0,3,5,9,12]
target = 9
print(binary_search(nums, target))

# Time Complexity: O(log n)

##########################  2. Find the Duplicate Number  ########################## 

# Q 2. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Floyd's Tortoise and Hare (Cycle Detection) algorithm.
#---------------------- Solution -----------------------------# 

def duplicate_number(nums):
    tortoise = nums[0]
    hare = nums[0]

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
print(duplicate_number(nums))


##########################  3. Search Insert Position  ########################## 

# Q 3. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,2,2,3,4,6]  , target = 5
# Output: 2
#---------------------- Solution -----------------------------# 

def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

    
nums = [1,2,2,3,4,6]  
target = 5
print(search_insert_position(nums, target))
# Time Complexity: O(log n)


##########################  4. Sort Colors  ########################## 

# Q 4. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same 
# color are adjacent, with the colors in the order red, white, and blue. 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#---------------------- Solution -----------------------------# 
def sort_color(nums):
    low, mid, high = 0, 0 , len(nums) -1

    while mid <=high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] ==1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -=1 
    return nums
nums = [2,0,2,1,1,0]
print(sort_color(nums))


##########################  5. Find First and Last Position of Element in Sorted Array  ########################## 

# Q 5. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position 
# of a given target value. If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

#---------------------- Solution -----------------------------# 
def find_first_last(nums, target):
    def find_first():
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid] == target:
                    first = mid
                right = mid - 1
        return first

    def find_last():
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    last = mid
                left = mid + 1
        return last

    first = find_first()
    last = find_last()

    return [first, last]


nums = [5,7,7,8,8,10]
target = 8
print(find_first_last(nums, target))


def find_first_last(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # search left half
                else:
                    left = mid + 1   # search right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound

    first = find_bound(is_first=True)
    last = find_bound(is_first=False)
    return [first, last]

nums = [5,7,7,8,8,10]
target = 8
print(find_first_last(nums, target))  # Output: [3,4]


##########################  6. Length of Last Word  ########################## 

# Q 6. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
#---------------------- Solution -----------------------------# 

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
print(length_of_last_word(s))
##########################  7. Set Matrix Zeroes  ########################## 


# Q 7. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

#---------------------- Solution -----------------------------# 


def set_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    rows_to_zero = set()
    cols_to_zero = set()
    
    # Step 1: Record rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    
    # Step 2: Zero out the required rows and columns
    for i in range(rows):
        for j in range(cols):
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j] = 0

    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zeroes(matrix))

##########################  8. Pascal's Triangle  ########################## 

# Q 8. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#---------------------- Solution -----------------------------# 



##########################  9. Single Element in a Sorted Array  ########################## 

# Q 9. Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once. Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
#---------------------- Solution -----------------------------# 


##########################  10. Search a 2D Matrix  ########################## 

# Q 10. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# • Each row is sorted in non-decreasing order.
# • The first integer of each row is greater than the last integer of then previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 11. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 


# Q 12. Find a Peak Element II
# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the 
# left, right, top, and bottom. Given a 0-indexed m x n matrix mat where no two adjacent cells are equal,
# find any peak element mat[i][j] and return the length 2 array [i,j].
# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

# Example 1:
# Input: mat = [[1,4],[3,2]]
# Output: [0,1]

#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 13. Max Value of Equation
# You are given an array points containing the coordinates of points on a 2D
# plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1
# <= i < j <= points.length. You are also given an integer k.
# Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k
# and 1 <= i < j <= points.length.
# It is guaranteed that there exists at least one pair of points that satisfy the
# constraint |xi - xj| <= k.

# Example 1:
# Input: x = [[1,3],[2,0],[5,10],[6,-10]], k = 1, n = 1
# Output: 4

#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 14. Jump Game
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true

#---------------------- Solution -----------------------------# 



##########################  4. Sort Colors  ########################## 

# Q 15.  Two Sum
# Given an array of integers nums and an integer target. Find two
# distinct indices i and j such that the sum of nums[i] and nums[j] is equal to the target.

#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 16. Contains Duplicate
# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is distinct.

#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 17. Best Time To Buy And Sell Stock
# Given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 18. Valid Parentheses
# Determine if an input string containing only the characters '(', ')',
# '{', '}', '[', and ']' is valid. A string is considered valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Each close bracket has a corresponding open bracket of the same type


#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 

# Q 19. Maximum Sum Subarray Of Size K
# Given an array of positive numbers and a positive number 'k,' find
# the maximum sum of any contiguous subarray of size 'k'.


#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 

# Q 20. Product Of Array Except Self
# Given an array of integers, return a new array where each
# element at index i of the new array is the product of all the
# numbers in the original array except the one at I
# .

#---------------------- Solution -----------------------------# 


##########################  4. Sort Colors  ########################## 

# Q 21. Triplet Sum To Zero
# Given an array of unsorted numbers, find all unique triplets in it
# that add up to zero.

#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 

# Q 22. Merge Intervals
# Given a list of intervals, merge all the overlapping intervals to
# produce a list that has only mutually exclusive intervals.

#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 

# Q 23. Group Anagrams
# Given a list of strings, the task is to group the anagrams together.
# An anagram is a word or phrase formed by rearranging the letters
# of another, such as "cinema", formed from "iceman".


#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 

# Q 24. Maximum Product Subarray
# Given an integer array, find the contiguous subarray (at least one
# number in it) that has the maximum product. Return this maximum product.

#---------------------- Solution -----------------------------# 

##########################  4. Sort Colors  ########################## 

# Q 25 Find Minimum In Rotated Sorted Array
# Given an array of numbers which is sorted in ascending order and
# also rotated by some arbitrary number, find if a given ‘key’ is present in it.
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, 
# return -1. You can assume that the given array does not have any duplicates.




# Array & Searching (Easy → Medium)


# Find First and Last Position of Element in Sorted Array – Start & end of target.

# Input: [5,7,7,8,8,10], target=8 → [3,4]

# Difficulty: Medium, O(log n)

# Single Element in a Sorted Array – Every element twice except one.

# Input: [1,1,2,3,3,4,4,8,8] → 2

# Difficulty: Medium, O(log n)

# Search a 2D Matrix – Row-wise sorted, first element of row > last of previous row.

# Input: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 → true

# Difficulty: Medium, O(log(m*n))

# Find Minimum in Rotated Sorted Array – Target in rotated sorted array.

# Input: [4,5,6,7,0,1,2], target=0 → 4

# Difficulty: Medium, O(log n)

# Array Problems (Easy → Medium)

# Two Sum – Indices i,j with nums[i]+nums[j]=target.

# Input: [2,7,11,15], target=9 → [0,1]

# Difficulty: Easy, O(n)

# Contains Duplicate – Check if any element repeats.

# Input: [1,2,3,1] → true

# Difficulty: Easy, O(n)

# Best Time to Buy and Sell Stock – Max profit from one transaction.

# Input: [7,1,5,3,6,4] → 5

# Difficulty: Easy, O(n)

# Sliding Window / Sum / Product (Medium)

# Maximum Sum Subarray of Size K – Max sum of contiguous subarray of size k.

# Input: [2,1,5,1,3,2], k=3 → 9

# Difficulty: Medium, O(n)

# Product of Array Except Self – New array, product of all except current element.

# Input: [1,2,3,4] → [24,12,8,6]

# Difficulty: Medium, O(n)

# Triplet Sum to Zero – All unique triplets adding to 0.

# Input: [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]

# Difficulty: Medium, O(n²)

# Maximum Product Subarray – Max product of contiguous subarray.

# Input: [2,3,-2,4] → 6

# Difficulty: Medium, O(n)

# Merge Intervals – Merge overlapping intervals.

# Input: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

# Difficulty: Medium, O(n log n)

# Sort Colors – Array of 0,1,2 sorted in-place.

# Input: [2,0,2,1,1,0] → [0,0,1,1,2,2]

# Difficulty: Medium, O(n)

# Set Matrix Zeroes – If element=0, set row & col to 0 in-place.

# Input: [[1,1,1],[1,0,1],[1,1,1]] → [[1,0,1],[0,0,0],[1,0,1]]

# Difficulty: Medium, O(m*n)

# String Problems (Easy)

# Length of Last Word – Length of last word.

# Input: "Hello World" → 5

# Difficulty: Easy, O(n)

# Valid Parentheses – Check if brackets are valid.

# Input: "([)]" → false

# Difficulty: Easy, O(n)

# DP / Triangle / Advanced 2D (Medium → Hard)

# Pascal's Triangle – Return first numRows of triangle.

# Input: 5 → [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Difficulty: Medium, O(numRows²)

# Find a Peak Element II – Peak in 2D grid (greater than top,bottom,left,right).

# Input: [[1,4],[3,2]] → [0,1]

# Difficulty: Hard, O(m log n)

# Max Value of Equation – Max yi+yj+|xi-xj| with |xi-xj| ≤ k.

# Input: [[1,3],[2,0],[5,10],[6,-10]], k=1 → 4

# Difficulty: Hard, O(n)

# Jump Game – Can you reach last index from first using max jumps.

# Input: [2,3,1,1,4] → true

# Difficulty: Medium, O(n)