# Q 1. Delete Node in a Linked List
# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the
# first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given
# node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean
# removing it from memory. We mean:
# • The value of the given node should not exist in the linked list.
# • The number of nodes in the linked list should decrease by one.
# • All the values before node should be in the same order.
# • All the values after node should be in the same order.
# Custom testing:
# • For the input, you should provide the entire linked list head and the node
# to be given node. node should not be the last node of the list and should
# be an actual node in the list.
# • We will build the linked list and pass the node to your function.
# • The output will be the entire list after calling your function.
# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]


# Q 2. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked
# list.
# If there are two middle nodes, return the second middle node.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]


# Q 3. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed
# list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Q 4. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in
# it.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer. Internally, pos is
# used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true

# Q 5. Remove Linked List Elements
# remove all the nodes of the linked list that has Node.val == val, and return the
# new head.
# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]


# Q 6. Linked List Cycle ||
# Given the head of a linked list, return the node where the cycle begins. If
# there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer. Internally, pos is
# used to denote the index of the node that tail's next pointer is connected to
# (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a
# parameter.
# Do not modify the linked list.
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1


# Q 7. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Q 8. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


# Q 9. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a Palindrome or false
# otherwise.
# Example 1:
# Input: head = [1,2,2,1]
# Output: true


# Q 11. Remove Duplicates from Sorted List II
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the linked
# list sorted as well.
# Example 1:
# Input: list1 = [1,2,3,4,5]
# Output: [1,2,5]


# Q 12. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
