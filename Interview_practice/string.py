####################### Q1. Remove Outermost Parentheses ######################

#  Q 1. Remove Outermost Parentheses
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and
# B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not
# exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s =
# P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"

#-------------------------------- Solution ----------------------------------#
# Solution 1: Depth Counter
def remove_outermost_parentheses(s: str) -> str:
    res = []
    depth = 0
    for ch in s:
        if ch == '(':
            if depth > 0: res.append(ch)
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth > 0: res.append(ch)
    return "".join(res)

print("Q1 Solution 1:", remove_outermost_parentheses("(()())(())"))

# Solution 2: Using Stack
def remove_outermost_parentheses_stack(s: str) -> str:
    stack, res = [], []
    for ch in s:
        if ch == '(':
            if stack: res.append(ch)
            stack.append(ch)
        elif ch == ')':
            stack.pop()
            if stack: res.append(ch)
    return "".join(res)

print("Q1 Solution 2:", remove_outermost_parentheses_stack("(()())(())"))

# Time Complexity: O(n)
# Space Complexity: O(n)


###################### Q2. Reverse Words in a String ######################

# Q 2. Reverse Words in a String
# Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Manual Traversal
def reverse_words_manual(s: str) -> str:
    words, word = [], ""
    for ch in s:
        if ch != " ": 
            word += ch
        elif word: 
            words.append(word)
            word = ""
    if word: 
        words.append(word)
    return " ".join(reversed(words))

print("Q2 Solution 1:", reverse_words_manual("  the sky  is blue "))

# Solution 2: Pythonic Split & Reverse

def reverse_words_pythonic(s: str) -> str:
    return " ".join(reversed(s.split()))

print("Q2 Solution 2:", reverse_words_pythonic("  the sky  is blue "))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 3: Manual Traversal using string

def reverse_words_manual_stirng(s):

    res = ""
    temp = ""
    for ch in s:
        if ch == " ":
            res = temp + " "+ res
            temp = ''
        else:
            temp += ch
    return temp + " "+ res

s = "  the sky  is blue "
print("Q2 Solution 3:", reverse_words_manual_stirng("  the sky  is blue "))


###################### Q3. Integer to Roman ######################

# Q 3. Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is written
# as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as
# IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six
# instances where subtraction is used:
# • I can be placed before V (5) and X (10) to make 4 and 9.
# • X can be placed before L (50) and C (100) to make 40 and 90.
# • C can be placed before D (500) and M (1000) to make 400 and 900.
# • Given an integer, convert it to a roman numeral.

# Example 1:
# Input: num = 3
# Output: "| | |"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Greedy Subtraction
def integer_to_roman(num: int) -> str:
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res = ""
    for i in range(len(val)):
        while num >= val[i]:
            res += syms[i]
            num -= val[i]
    return res

print("Q3 Solution 1:", integer_to_roman(1994))

# Solution 2: Predefined Thousands/Hundreds/Tens/Ones

def integer_to_roman_predefined(num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[num//1000] + hundreds[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]

print("Q3 Solution 2:", integer_to_roman_predefined(1994))

# Time Complexity: O(1)
# Space Complexity: O(1)

###################### Q4. Simplify Path ######################

# Q 4. Simplify Path
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given a string path, which is an absolute path (starting with a slash '/') to a
# file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a double
# period '..' refers to the directory up a level, and any multiple consecutive
# slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other
# format of periods such as '...' are treated as file/directory names.
# • The canonical path should have the following format:
# • The path starts with a single slash '/'.
# • Any two directories are separated by a single slash '/'.
# • The path does not end with a trailing '/'.
# • The path only contains the directories on the path from the root
# directory to the target file or directory (i.e., no period '.' or double period '..') 
# Return the simplified canonical path.

# Example 1:
# Input: path = "/home/"
# Output: "/home"
#-------------------------------- Solution ----------------------------------#


def simplify_path(path):
    stack = []
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)
    return "/" + "/".join(stack)

path = "/a/./b/../../c/"
print("Q4:", simplify_path(path))  # Output: "/c"

# Time Complexity: O(n)
# Space Complexity: O(n)


###################### Q5. Longest Palindromic Substring ######################

# Q 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Brute Force

def longest_palindrome_brute(s: str) -> str:
    lp = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(lp):
                lp = sub
    return lp

print("Q5 Solution 1:", longest_palindrome_brute("babad"))

# Solution 2: Expand Around Center (Optimized)
def longest_palindrome_center(s: str) -> str:
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        res = max(res, expand(i, i), expand(i, i+1), key=len)
    return res

print("Q5 Solution 2:", longest_palindrome_center("babad"))

# Time Complexity: O(n^2)
# Space Complexity: O(1)


###################### Q6. Isomorphic Strings ######################


# Q 6. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

#-------------------------------- Solution ----------------------------------#

# Approach: Two-way mapping
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_map, t_map = {}, {}
    for cs, ct in zip(s, t):
        if (cs in s_map and s_map[cs] != ct) or (ct in t_map and t_map[ct] != cs):
            return False
        s_map[cs] = ct
        t_map[ct] = cs
    return True

print("Q6:", is_isomorphic("egg", "add"))  # Output: True

# Time Complexity: O(n)
# Space Complexity: O(n)



###################### Q7. Longest Common Prefix ######################

# Q 7. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Horizontal Scanning

def longest_common_prefix(strs: list) -> str:
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return ""
    return prefix

print("Q7 Solution 1:", longest_common_prefix(["flower","flow","flight"]))


# Solution 2: Sorting & Compare First/Last

def longest_common_prefix_sort(strs: list) -> str:
    if not strs: return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < min(len(first), len(last)) and first[i] == last[i]:
        i += 1
    return first[:i]

print("Q7 Solution 2:", longest_common_prefix_sort(["flower","flow","flight"]))

# Time Complexity: O(S) total chars, 
# Space Complexity: O(1)


###################### Q8. Valid Palindrome II ######################


# Q 8. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
# Input: s = "aba"
# Output: true

#-------------------------------- Solution ----------------------------------#

# Solution 1: reverse string
def valid_palindrome_using_revserse(s):
    return s == s[::-1]
    
s = "aba"
print("Q8 Solution 1:", valid_palindrome_using_revserse("abca"))


# Solution 2: Check by Removing Each Character (Brute Force)
def valid_palindrome_brute(s: str) -> bool:
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return True
    return s == s[::-1]

print("Q8 Solution 1:", valid_palindrome_brute("abca"))

# Solution 3: Two Pointers (Optimized)
def valid_palindrome_two_pointers(s: str) -> bool:
    def is_palindrome_range(l, r):
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True

    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome_range(l+1, r) or is_palindrome_range(l, r-1)
        l += 1
        r -= 1
    return True

print("Q8 Solution 2:", valid_palindrome_two_pointers("abca"))


# Time Complexity: O(n)
# Space Complexity: O(1)



###################### Q9. Index of First Occurrence ######################

# Q 9. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence
# of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

#-------------------------------- Solution ----------------------------------#

# Solution 1: Sliding Window / Slicing

def first_occurrence(haystack: str, needle: str) -> int:
    if not needle: return 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print("Q9 Solution 1:", first_occurrence("sadbutsad", "sad"))


# Solution 2: Python Built-in find (Simple)
def first_occurrence_builtin(haystack: str, needle: str) -> int:
    return haystack.find(needle)

print("Q9 Solution 2:", first_occurrence_builtin("sadbutsad", "sad"))

# Time Complexity: O((N-L)L) for manual, O(N) avg for built-in
# Space Complexity: O(1)


###################### Q10. Basic Calculator II ######################

# Q 10. Basic Calculator II
# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

#-------------------------------- Solution ----------------------------------#

# Solution 1: Stack-Based Evaluation

def basic_calculator(s):
    s = s.replace(" ", "")
    stack, num, sign = [], 0, "+"
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num*10 + int(ch)
        if ch in "+-*/" or i == len(s)-1:
            if sign == "+": stack.append(num)
            elif sign == "-": stack.append(-num)
            elif sign == "*": stack.append(stack.pop()*num)
            elif sign == "/": stack.append(int(stack.pop()/num))
            sign = ch
            num = 0
    return sum(stack)

s = "3+2*2"
print("Q10:", basic_calculator(s))  # Output: 7

# Solution 2: Without Stack (Two Variables)

def basic_calculator_no_stack(s: str) -> int:
    s = s.replace(" ", "")
    res, last_num, num, sign = 0, 0, 0, "+"
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num*10 + int(ch)
        if ch in "+-*/" or i == len(s)-1:
            if sign == '+': res, last_num = res + last_num, num
            elif sign == '-': res, last_num = res + last_num, -num
            elif sign == '*': last_num *= num
            elif sign == '/': last_num = int(last_num / num)
            sign = ch
            num = 0
    return res + last_num

print("Q10 Solution 2:", basic_calculator_no_stack("3+2*2"))

# Time Complexity: O(n)
# Space Complexity: O(n) or O(1) depending on approach


###################### Q11. Largest Odd Number in String ######################

# Q 11. Largest Odd Number in String
# You are given a string num, representing a large integer. Return the largest-
# valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: num = "52"
# Output: "5"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Brute Force

def largest_odd_number_string(num):

    res = []
    for i in num:
        if int(i) % 2 !=0:
            res.append(int(i))
    
    return max(res)

num = "52"
print("Q11 Solution 1:", largest_odd_number_string("52"))

# Solution 2: Scan from End (Optimized)

def largest_odd_number(num: str) -> str:
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""

print("Q11 Solution 2:", largest_odd_number("52"))


# Solution 3: Collect All Odd Substrings (Brute Force)

def largest_odd_number_brute(num: str) -> str:
    res = ""
    for i in range(len(num)):
        for j in range(i+1, len(num)+1):
            if int(num[j-1]) % 2 != 0 and int(num[i:j]) > int(res or "0"):
                res = num[i:j]
    return res

print("Q11 Solution 3:", largest_odd_number_brute("52"))

# Time Complexity: O(n) for optimized, O(n^2) for brute force
# Space Complexity: O(1)

###################### Q12. Count and Say ######################


# Q 12. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# • countAndSay(n) is the way you would "say" the digit string from
# • countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of
# substrings such that each substring contains exactly one unique digit. Then
# for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
# For example, the saying and conversion for digit string "3322251":

# Example 1:
# Given a positive integer n, return the nth term of the count-and-say sequence.
# Input: n = 1
# Output: "1"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Iterative Build
def count_and_say(n: int) -> str:
    res = "1"
    for _ in range(n-1):
        new_res, count = "", 1
        for i in range(1, len(res)+1):
            if i < len(res) and res[i] == res[i-1]:
                count += 1
            else:
                new_res += str(count) + res[i-1]
                count = 1
        res = new_res
    return res

print("Q12 Solution 1:", count_and_say(5))

# Solution 2: Using groupby from itertools (Pythonic)
from itertools import groupby

def count_and_say_groupby(n: int) -> str:
    res = "1"
    for _ in range(n-1):
        res = "".join([str(len(list(g))) + k for k, g in groupby(res)])
    return res

print("Q12 Solution 2:", count_and_say_groupby(5))


# Time Complexity: O(2^n) approximately
# Space Complexity: O(2^n)

###################### Q13. Minimum Window Substring ######################

# Q 13. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

#-------------------------------- Solution ----------------------------------#

# Solution 1: Sliding Window + Hashmap
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t: return ""
    t_count = Counter(t)
    required = len(t_count)
    l, formed = 0, 0
    window_count = {}
    ans = float("inf"), None, None
    
    for r, ch in enumerate(s):
        window_count[ch] = window_count.get(ch, 0) + 1
        if ch in t_count and window_count[ch] == t_count[ch]:
            formed += 1
        while l <= r and formed == required:
            if r-l+1 < ans[0]:
                ans = (r-l+1, l, r)
            window_count[s[l]] -= 1
            if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                formed -= 1
            l += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

print("Q13 Solution 1:", min_window("ADOBECODEBANC", "ABC"))


#Time Complexity: O(|s| + |t|)
# Space Complexity: O(|s| + |t|)


###################### Q14. Valid Anagram ######################

# Q 14. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

#-------------------------------- Solution ----------------------------------#

# Solution 1: Sorting

def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print("Q14 Solution 1:", is_anagram_sort("anagram", "nagaram"))

# Solution 2: Hashmap / Counter
from collections import Counter

def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print("Q14 Solution 2:", is_anagram_counter("anagram", "nagaram"))


# Time Complexity: O(n)
# Space Complexity: O(n)
