# Q 1. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2

# Q 2. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and
# return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Input: nums = [2,3,-2,4]
# Output: 6

# Q 3. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# Input: s = "babad"
# Output: "bab"

# Q 4. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return
# its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


# Q 5. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4

# Q 6. Ones and Zeroes
# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's
# and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4

# Q 7. Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each i (0
# <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Q 8. Knight Dialer
# The chess knight has a unique movement, it may move two squares vertically
# and one square horizontally, or two squares horizontally and one square
# vertically (with both forming the shape of an L). The possible movements of
# chess knight are shown in this diagaram:
# A chess knight can move as indicated in the chess diagram below:
# We have a chess knight and a phone pad as shown below, the knight can only
# stand on a numeric cell (i.e. blue cell).
# Page: 60Given an integer n, return how many distinct phone numbers of length n we
# can dial.
# You are allowed to place the knight on any numeric cell initially and then you
# should perform n - 1 jumps to dial a number of length n. All jumps should be
# valid knight jumps.
# As the answer may be very large, return the answer modulo 109 + 7.
# Example 1:
# Input: n = 1
# Output: 10


# Q 9. Coin Change
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# You may assume that you have an infinite number of each kind of coin.
# Example1:
# Input: coins = [1,2,5], amount = 11
# Output: 3

# Q 10. Partition Equal Subset Sum
# Given an integer array nums, return true if you can partition the array into two
# subsets such that the sum of the elements in both subsets is equal or false
# otherwise.
# Example1:
# Input: nums = [1,5,11,5]
# Output: true


# Q 11. Minimum Cost to Cut a Stick
# Given a wooden stick of length n units. The stick is labelled from 0 to n. For
# example, a stick of length 6 is labelled as follows:
# Given an integer array cuts where cuts[i] denotes a position you should
# perform a cut at.
# You should perform the cuts in order, you can change the order of the cuts as
# you wish.
# The cost of one cut is the length of the stick to be cut, the total cost is the
# sum of costs of all cuts. When you cut a stick, it will be split into two smaller
# sticks (i.e. the sum of their lengths is the length of the stick before the cut).
# Please refer to the first example for a better explanation.
# Return the minimum total cost of the cuts.
# Example 1:
# Input: n = 7, cuts = [1,3,4,5]
# Output: 16

# Q 12. Best Time to Buy and Sell Stock with Cooldown
# You are given an array prices where prices[i] is the price of a given stock on
# the ith day.
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock multiple
# times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown
# one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3

# Q 13. Best Time to Buy and Sell Stock with Transaction Fee
# You are given an array prices where prices[i] is the price of a given stock on
# the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like, but you need to pay the transaction fee for each
# transaction.
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Page: 63Page: 64Page: 65