# Q 1. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000


# Q 2. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−231, 231 − 1]. For this
# problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and
# if the quotient is strictly less than -231, then return -231.
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3


# Q 3. Most Beautiful Item for Each Query
# You are given a 2D integer array items where items[i] = [pricei, beautyi]
# denotes the price and beauty of an item respectively.
# You are also given a 0-indexed integer array queries. For each queries[j], you
# want to determine the maximum beauty of an item whose price is less than
# or equal to queries[j]. If no such item exists, then the answer to this query is
# 0.
# Return an array answer of the same length as queries where answer[j] is the
# answer to the jth query.
# Example 1:
# Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
# Output: [2,4,5,5,6,6]

# Q 4. Minimum Absolute Sum Difference
# You are given two positive integer arrays nums1 and nums2, both of length n.
# The absolute sum difference of arrays nums1 and nums2 is defined as the
# sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).
# You can replace at most one element of nums1 with any other element in
# nums1 to minimize the absolute sum difference.
# Return the minimum absolute sum difference after replacing at most one
# element in the array nums1. Since the answer may be large, return it modulo
# 109 + 7.
# |x| is defined as:
# • x if x >= 0, or
# • -x if x < 0.
# Example 1:
# Input: nums1 = [1,7,5], nums2 = [2,3,5]
# Output: 3
