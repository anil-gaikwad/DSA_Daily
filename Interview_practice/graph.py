##########################  1. Number of Islands ########################## 
# Q 1. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input: grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]
# Output: 1

#--------------------------- Solution --------------------------------# 


##########################  2. Network Delay Time ########################## 

# Q 2. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, 
# a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is
# the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes
# for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
#--------------------------- Solution --------------------------------# 


##########################  3. Decode String ########################## 

# Q 3. Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

#--------------------------- Solution --------------------------------# 


##########################  4. Shortest Bridge ########################## 

# Q 4. Shortest Bridge
# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island.
# Return the smallest number of 0's you must flip to connect the two islands.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 1

#--------------------------- Solution --------------------------------# 


##########################  5. Cheapest Flights Within K Stops ########################## 

# Q 5. Cheapest Flights Within K Stops
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates 
# that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
# If there is no such route, return -1.

# Example 1:
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0,
# dst = 3, k = 1
# Output: 700

#--------------------------- Solution --------------------------------# 


##########################  6. Remove Boxes ########################## 

# Q 6. Remove Boxes
# You are given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (i.e.,
# composed of k boxes, k >= 1), remove them and get k * k points. Return the maximum points you can get.

# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23

#--------------------------- Solution --------------------------------# 


##########################  7. Maximum Number of Non-Overlapping Substrings ########################## 

# Q 7. Maximum Number of Non-Overlapping Substrings
# Given a string s of lowercase letters, you need to find the maximum number
# of non-empty substrings of s that meet the following conditions:
# The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
# A substring that contains a certain character c must also contain all occurrences of c.
# Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number 
# of substrings, return the one with minimum total length. It can be shown that there exists a unique
# solution of minimum total length.
# Notice that you can return the substrings in any order.

# Example 1:
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the conditions:
# ["adefaddaccc", "adefadda","ef", "e", "f", "ccc"]
#--------------------------- Solution --------------------------------# 


##########################  8. Find Eventual Safe States ########################## 
# Q 8. Find Eventual Safe States
# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i]
# is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
# A node is a terminal node if there are no outgoing edges. A node is a safe
# node if every possible path starting from that node leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

# Example 1:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]

#--------------------------- Solution --------------------------------# 


##########################  9. Word Ladder ########################## 

# Q 9. Word Ladder
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
# • Every adjacent pair of words differs by a single letter.
# • Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# • sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
# shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Input: beginWord = "hit", endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5

#--------------------------- Solution --------------------------------# 


##########################  10. Threshold Distance ########################## 

# Q 10. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents 
# a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through
# some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with 
# the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

# Example 1:
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3

#--------------------------- Solution --------------------------------# 


##########################  11. Minimum Cost ########################## 

# Q 11. Minimum Cost to Make at Least One Valid Path in a Grid
# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell
# you should visit if you are currently in this cell. The sign of grid[i][j] can be:
# • 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j+ 1])
# • 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j -1])
# • 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# • 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.
# You will initially start at the upper left cell (0, 0). A valid path in the grid is a
# path that starts from the upper left cell (0, 0) and ends at the bottom-right cell
# (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
# Return the minimum cost to make the grid have at least one valid path.

# Example 1:
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
#--------------------------- Solution --------------------------------# 
