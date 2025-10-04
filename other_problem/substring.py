######################  STRING / SUBSTRING INTERVIEW PROBLEMS #####################
# This file contains common string problems with solutions.
# Each function is commented with input, output, and approach.
###################################################################################

######################  1. Generate all substrings ###############################
def all_substrings(s):
    """
    Generate all substrings of a string.
    Input: "abc"
    Output: ["a", "ab", "abc", "b", "bc", "c"]
    Approach: Nested loops or slicing.
    """
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

######################  2. Check if substring exists ############################
def is_substring(s, sub):
    """
    Check if a string is a substring of another.
    Input: "hello", "ell"
    Output: True
    Approach: Use 'in' operator.
    """
    return sub in s

######################  3. First occurrence of substring #######################
def first_occurrence_string(s, sub):
    """
    Find the first occurrence of a substring.
    Input: "hello world", "world"
    Output: 6 (index)
    Approach: Naive search or str.find()
    """
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1

######################  4. Count occurrences of substring ######################
def count_occurrences_substring(s, sub):
    """
    Count occurrences of a substring.
    Input: "abababa", "aba"
    Output: 3
    Approach: Sliding window
    """
    cnt = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            cnt += 1
    return cnt

######################  5. Count distinct substrings ##########################
def count_distinct_substring(s):
    """
    Count distinct substrings of a string.
    Input: "ababa"
    Output: 9
    Approach: Use a set to store all substrings.
    """
    n = len(s)
    substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(s[i:j])
    return len(substrings)

######################  6. Count all palindromic substrings ##################
def count_palindromic_string(s):
    """
    Count all palindromic substrings.
    Input: "aaa"
    Output: 6
    Approach: Expand around centers
    """
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                cnt += 1
    return cnt

######################  7. Longest palindromic substring #####################
def longest_palindrome_string(s):
    """
    Find longest palindromic substring.
    Input: "babad"
    Output: "bab" or "aba"
    Approach: Expand around center
    """
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub
    return longest

######################  8. Check if strings are rotations ###################
def string_rotations(s, sub):
    """
    Check if one string is a rotation of another.
    Input: "abcde", "cdeab"
    Output: True
    Approach: Concatenate first string and check substring.
    """
    return len(s) == len(sub) and sub in (s + s)

######################  9. Substring with maximum frequency ################
def substring_max_frequency(s):
    """
    Find substring with maximum frequency.
    Input: "ababab"
    Output: "ab"
    Approach: Use a hashmap to store frequencies
    """
    freq_map = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            freq_map[sub] = freq_map.get(sub,0)+1
    max_freq = max(freq_map.values())
    max_sub = max((sub for sub, freq in freq_map.items() if freq==max_freq), key=len)
    return max_sub

######################  10. Smallest substring containing all chars ########

def smallest_substring_array(s, t):
    """
    Input: s="ADOBECODEBANC", t="ABC" 
    Output: "BANC" 
    Approach: Two Pointers + Frequency Array
    """
    need = [0] * 128
    have = [0] * 128
    for ch in t:
        need[ord(ch)] += 1

    required = sum(1 for x in need if x > 0)
    formed = 0
    left = 0
    min_len = float("inf")
    min_sub = ""

    for right, ch in enumerate(s):
        have[ord(ch)] += 1
        if need[ord(ch)] > 0 and have[ord(ch)] == need[ord(ch)]:
            formed += 1

        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_sub = s[left:right+1]

            have[ord(s[left])] -= 1
            if need[ord(s[left])] > 0 and have[ord(s[left])] < need[ord(s[left])]:
                formed -= 1
            left += 1

    return min_sub


def smallest_substring_bruteforce(s, t):
    """
    Input: s="ADOBECODEBANC", t="ABC" 
    Output: "BANC" 
    Approach: Brute Force
    """
     
    from collections import Counter

    t_count = Counter(t)
    n = len(s)
    min_sub = None

    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if not t_count - Counter(sub):  # check if sub covers all of t
                if min_sub is None or len(sub) < len(min_sub):
                    min_sub = sub
    return min_sub if min_sub else ""


######################  11. Longest substring without repeating characters
def longest_unique_substring(s):
    """
    Longest substring without repeating characters.
    Input: "abcabcbb"
    Output: 3 ("abc")
    Approach: Sliding window + set
    """
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len

######################  12. Longest substring with at most K distinct chars
def longest_substring_k_distinct(s, k):
    """
    Longest substring with at most K distinct characters.
    Input: "eceba", K=2
    Output: 3 ("ece")
    Approach: Sliding window + hashmap
    """
    left = 0
    max_len = 0
    char_map = {}
    for right in range(len(s)):
        char_map[s[right]] = char_map.get(s[right],0)+1
        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]]==0:
                del char_map[s[left]]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len

######################  13. Longest substring with equal 0s and 1s
def longest_equal_0s_1s(s):
    """
    Longest substring with equal number of 0s and 1s (binary string)
    Input: "1101010"
    Output: 6
    Approach: Prefix sum + hashmap
    """
    prefix_sum = 0
    index_map = {0:-1}
    max_len = 0
    for i,ch in enumerate(s):
        prefix_sum += 1 if ch=='1' else -1
        if prefix_sum in index_map:
            max_len = max(max_len, i-index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i
    return max_len

######################  14. Longest repeated substring ####################
def longest_repeated_substring(s):
    """
    Longest repeated substring
    Input: "banana"
    Output: "ana"
    Approach: Suffix array + hashmap
    """
    freq_map = {}
    longest = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub = s[i:j]
            freq_map[sub] = freq_map.get(sub,0)+1
            if freq_map[sub]>1 and len(sub)>len(longest):
                longest=sub
    return longest

######################  15. Lexicographically smallest substring of length k
def smallest_substring_k(s,k):
    """
    Lexicographically smallest substring of length k
    Input: "leetcode", k=3
    Output: "cod"
    Approach: Sliding window
    """
    n = len(s)
    if k>n: return ""
    smallest = s[:k]
    for i in range(1,n-k+1):
        curr = s[i:i+k]
        if curr<smallest:
            smallest = curr
    return smallest

######################  16. Max product of lengths of two non-overlapping substrings
def max_product_nonoverlap_substrings(s):
    """
    Maximum product of lengths of two non-overlapping substrings without common characters
    Input: "abcwdefgh"
    Output: 16
    Approach: Bitmasking
    """
    n = len(s)
    masks = []
    for i in range(n):
        mask = 0
        for j in range(i,n):
            char = ord(s[j])-ord('a')
            if (mask>>char)&1: break
            mask |= 1<<char
            masks.append((mask,j-i+1))
    max_product = 0
    for i in range(len(masks)):
        for j in range(i+1,len(masks)):
            if masks[i][0]&masks[j][0]==0:
                max_product = max(max_product,masks[i][1]*masks[j][1])
    return max_product

######################  DEMO #######################
if __name__ == "__main__":
    print("1. All substrings:", all_substrings("abc"))
    print("2. Is substring:", is_substring("hello","ell"))
    print("3. First occurrence:", first_occurrence_string("hello world","world"))
    print("4. Count occurrences:", count_occurrences_substring("abababa","aba"))
    print("5. Distinct substrings:", count_distinct_substring("ababa"))
    print("6. Count palindromic substrings:", count_palindromic_string("aaa"))
    print("7. Longest palindrome substring:", longest_palindrome_string("babad"))
    print("8. String rotations:", string_rotations("abcde","cdeab"))
    print("9. Substring with max frequency:", substring_max_frequency("ababab"))
    print("10. smallest substring array:", smallest_substring_array("ADOBECODEBANC","ABC"))
    print("11. Longest unique substring:", longest_unique_substring("abcabcbb"))
    print("12. Longest substring with K distinct chars:", longest_substring_k_distinct("eceba",2))
    print("13. Longest equal 0s and 1s:", longest_equal_0s_1s("1101010"))
    print("14. Longest repeated substring:", longest_repeated_substring("banana"))
    print("15. Smallest substring of length k:", smallest_substring_k("leetcode",3))
    print("16. Max product non-overlapping substrings:", max_product_nonoverlap_substrings("abcwdefgh"))
