# 1> Generate all substrings of a string
# Input: "abc"
# Output: ["a", "ab", "abc", "b", "bc", "c"]
# Approach: Nested loops or slicing.

def all_substrings(s):
    n = len(s)
    sub_string = []
    for i in range(n):
        for j in range(i+1, n + 1):
            sub_string.append(s[i:j])
    
    return sub_string

s = "abc"
print(all_substrings(s))


# 2> Check if a string is a substring of another
# Input: "hello", "ell"
# Output: True
# Approach: Sliding window, brute force, or in operator.

def is_substring(s, sub):
    return sub in s

s = "hello"
sub = "ell"

print(is_substring(s, sub))


# 3> Find the first occurrence of a substring
# Input: "hello world", "world"
# Output: 6 (index)
# Approach: Naive search, KMP, or str.find().

def first_occurance_string(s, sub):
    for i in range(len(s) - len(sub) +1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1
    # return s.find(sub)

s = "hello world"
sub = "world"
print(first_occurance_string(s, sub))


# 4> Count occurrences of a substring
# Input: "abababa", "aba"
# Output: 3
# Approach: Sliding window, str.count().

def count_occurrences_substring(s, sub):
    cnt = 0

    for i in range(len(s)- len(sub)+1):
        if s[i:i+len(sub)] == sub:
            cnt +=1
    return cnt

s = "abababa"
sub = "aba"
print(count_occurrences_substring(s, sub))


# 5> Count distinct substrings
# Input: "ababa"
# Output: 9 distinct substrings
# Approach: Suffix array + LCP, or Trie.

def count_distinct_substring(s):
    n = len(s)
    sub_string = set()
    for i in range(n):
        for j in range(i+1, n + 1):
            sub_string.add(s[i:j])
    
    return len(sub_string)

s = "ababa"
print(count_distinct_substring(s))


# 6> Count all palindromic substrings
# Input: "aaa"
# Output: 6 ("a","a","a","aa","aa","aaa")
# Approach: Expand around center, DP.

def count_palindromic_string(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n +1):
            new_str = s[i:j]
            if new_str == new_str[::-1]:
                cnt += 1
    return cnt

s = "aaa"
print(count_palindromic_string(s))


# 7> Longest palindromic substring
# Input: "babad"
# Output: "bab" or "aba"
# Approach: Expand around center, Manacher’s Algorithm (O(n)).

def longest_palindrome_string(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i+1, n +1):
            new_str = s[i:j]
            if new_str == new_str[::-1] and len(new_str) > len(longest):
                longest = new_str
    return longest

s = "babad"
print(longest_palindrome_string(s))


# 8> Check if two strings are rotations (using substrings)
# Input: "abcde", "cdeab"
# Output: True
# Approach: Concatenate first string → "abcdeabcde", check substring.

def string_rotations(s, sub):
    if len(s) != len(sub):
        return False

    return sub in (s+s)


s = "abcde" 
sub = "cdeab"
print(string_rotations(s, sub))


# 9> Find substring with maximum frequency
# Input: "ababab"
# Output: "ab" occurs 3 times

def substring_max_frequency(s):
    maps = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            maps[sub] = maps.get(sub, 0) + 1

    max_freq = max(maps.values())
    max_sub = max((sub for sub, freq in maps.items() if freq == max_freq), key=len)
    return max_sub

s = "ababab"
print(substring_max_frequency(s))


# 10> Find smallest substring containing all characters of another string
# Input: s="ADOBECODEBANC", t="ABC"
# Output: "BANC"
# Approach: Sliding window + hashmap.

def smallest_substring(s, t):
    maps = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub.find(t):
                maps[sub] = maps.get(sub, 0) + 1

    return maps

s = "ADOBECODEBANC"
t = "ABC"
# print(smallest_substring(s, t))

# 11> Longest substring without repeating characters
# Input: "abcabcbb"
# Output: 3 ("abc")
# Approach: Sliding window + set.

def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

s = "abcabcbb"
print(longest_unique_substring(s))


# 12> Longest substring with at most K distinct characters
# Input: "eceba", K=2
# Output: 3 ("ece")
# Approach: Sliding window + hashmap.

def longest_substring_k_distinct(s, k):
    n = len(s)
    if not s and k ==0:
        return 0
    
    left = 0
    max_len = 0
    char_map = {}

    for right in range(len(s)):
        char_map[s[right]] = char_map.get(s[right], 0) + 1

        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]

            left +=1
        max_len = max(max_len, right -left + 1)
    
    return max_len

s = "eceba"
k = 2 
print(longest_substring_k_distinct(s, k))

# 13> Longest substring with equal number of 0s and 1s (binary string)
# Input: "1101010"
# Output: 6 ("101010")
# Approach: Prefix sum + hashmap.

def longest_equal_0s_1s(s):
    prefix_sum = 0
    index_map = {0: -1}  # prefix_sum -> first index
    max_len = 0

    for i, ch in enumerate(s):
        prefix_sum += 1 if ch == '1' else -1

        if prefix_sum in index_map:
            max_len = max(max_len, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i

    return max_len

s = "1101010"
print(longest_equal_0s_1s(s))

# 14> Longest repeated substring
# Input: "banana"
# Output: "ana"
# Approach: Suffix array + LCP.

def longest_repeated_substring(s):
    maps = {}
    longest = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            maps[sub] = maps.get(sub, 0) + 1
            if maps[sub] > 1 and len(sub) > len(longest):
                longest = sub
    
    return longest


s = "banana"
print(longest_repeated_substring(s))

# 15> Lexicographically smallest substring of length k
# Input: "leetcode", k=3
# Output: "cod"
# Approach: Sliding window / min-heap.

def smallest_substring_k(s, k):
    n = len(s)

    if  k > n:
        return ""
    
    smallest = s[:k]

    for i in range(1, n - k +1):
        current = s[i:i+k]
        if current < smallest:
            smallest = current

    return smallest

s = "leetcode"
k = 3
print(smallest_substring_k(s, k))


# 16> Maximum product of lengths of two non-overlapping substrings without common characters
# Input: "abcwdefgh"
# Output: 16 ("abcw" & "defgh")
# Approach: Bitmasking.

def max_product_nonoverlap_substrings(s):
    n = len(s)
    masks = []

    for i in range(n):
        mask = 0
        for j in range(i, n):
            char = ord(s[j]) - ord('a')
            if (mask >> char) & 1:
                break
            mask |= 1 << char
            masks.append((mask, j - i + 1))

    max_product = 0
    for i in range(len(masks)):
        for j in range(i + 1, len(masks)):
            if masks[i][0] & masks[j][0] == 0:
                max_product = max(max_product, masks[i][1] * masks[j][1])
    
    return max_product

s = "abcwdefgh"
print(max_product_nonoverlap_substrings(s))