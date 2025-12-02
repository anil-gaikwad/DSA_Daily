
########################## 11. Implement Queue using Stacks ########################## 
# Q 1. Implement Queue using Stacks
# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# • void push(int x) Pushes element x to the back of the queue.
# • int pop() Removes the element from the front of the queue and returns it.
# • int peek() Returns the element at the front of the queue.
# • boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
# • You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# • Depending on your language, the stack may not be supported natively.
# You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[ ], [1], [2], [ ], [ ], [ ]]
# Output
# [null, null, null, 1, 1, false]

#--------------------------- Solution --------------------------------# 

########################## 2. Implement Stack using Queues ########################## 

# Q 2. Implement Stack using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
# • void push(int x) Pushes element x to the top of the stack.
# • int pop() Removes the element on the top of the stack and returns it.
# • int top() Returns the element on the top of the stack.
# • boolean empty() Returns true if the stack is empty, false otherwise.

# Example 1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[ ], [1], [2], [ ], [ ], [ ]]
# Output
# [null, null, null, 2, 2, false]


#--------------------------- Solution --------------------------------# 

########################## 3. Backspace String Compare ########################## 

# Q 3. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true

#--------------------------- Solution --------------------------------# 

########################## 4. Valid Parentheses ########################## 

# Q 4. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true


#--------------------------- Solution --------------------------------# 

########################## 5. Min Stack ########################## 
# Q 5. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# • MinStack() initializes the stack object.
# • void push(int val) pushes the element val onto the stack.
# • void pop() removes the element on the top of the stack.
# • int top() gets the top element of the stack.
# • int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]

#--------------------------- Solution --------------------------------# 

########################## 6. Next Greater Element | ########################## 

# Q 6. Next Greater Element |
# The next greater element of some element x in an array is the first greater
# element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine 
# the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
#--------------------------- Solution --------------------------------# 


########################## 7. Largest Rectangle in Histogram ########################## 

# Q 7. Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10

#--------------------------- Solution --------------------------------# 

########################## 8. Online Stock Span ########################## 
# Q 8. Online Stock Span
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) 
# for which the stock price was less than or equal to the price of that day.
# • For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, 
# then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# • Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, 
# then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

# Implement the StockSpanner class:
# • StockSpanner() Initializes the object of the class.
# • int next(int price) Returns the span of the stock's price given that today's price is price.
# Example 1:
# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[ ], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

#--------------------------- Solution --------------------------------# 

########################## 9. Minimum Insertions to Balance a Parentheses String ########################## 

# Q 9. Minimum Insertions to Balance a Parentheses String
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.

# Example 1:
# Input s = "(()))"
# Output = 1

#--------------------------- Solution --------------------------------# 

########################## 10. 132 Pattern ########################## 

# Q 10. 132 Pattern
# Given an array of n integers nums, a 132 pattern is a subsequence of three
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: false

#--------------------------- Solution --------------------------------# 


########################## 11. Trapping Rain Water ########################## 

# Q 11. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output = 6

#--------------------------- Solution --------------------------------# 

########################## 12. Merge Intervals ########################## 
# Q 12. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
#--------------------------- Solution --------------------------------# 


########################## 13. Sum of Subarray Minimums ########################## 

# Q 13. Sum of Subarray Minimums
# Given an array of integers arr, find the sum of min(b), where b ranges over
# every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# Example 1:
# Input: arr = [3,1,2,4]
# Output = 17

#--------------------------- Solution --------------------------------# 


########################## 14. LRU Cache ########################## 

# Q 14. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]


#--------------------------- Solution --------------------------------# 


########################## 15. Remove K Digits ########################## 

# Q 15. Remove K Digits
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
#--------------------------- Solution --------------------------------# 


########################## 16. Rotting Oranges ########################## 

# Q 16. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:
# • 0 representing an empty cell,
# • 1 representing a fresh orange, or
# • 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

#--------------------------- Solution --------------------------------# 

########################## 17. Maximal Rectangle ########################## 

# Q 17. Maximal Rectangle
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area

# Example 1:
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
#--------------------------- Solution --------------------------------# 


########################## 18. Evaluate Reverse Polish Notation ########################## 

# Q 18. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic
# expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# • The valid operators are '+', '-', '*', and '/'.
# • Each operand may be an integer or another expression.
# • The division between two integers always truncates toward zero.
# • There will not be any division by zero.
# • The input represents a valid arithmetic expression in a reverse polish notation.
# • The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9

#--------------------------- Solution --------------------------------# 
