######################  LIST  #########################
## 1> In given list find the occurrence of each element.
# Input: list = [1,2,2,4,2,3,4,4,5,1]
# Output: {1: 2, 2: 3, 4: 4, 3: 1, 5: 1}

from collections import Counter
import numpy as np
import pandas as pd
### ------------------- ###
# solution [1]
def Solution1(lst):
    count_dict = Counter(lst)
    return dict(count_dict)

# solution [2]
def Solution2(lst):
    count_dict = {}

    for num in lst:
        if num in count_dict:
            count_dict[num] +=1
        else:
            count_dict[num] = 1
    return count_dict

# solution [3]
def Solution3(lst):
    return {num: lst.count(num) for num in set(lst)}

# solution [4]
def Solution4(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    return freq

# solution [5]
def Solution5(lst):
    nums = [1,2,2,4,2,3,4,4,5,1]
    unique, counts = np.unique(nums, return_counts=True)
    freq = dict(zip(unique.tolist(), counts.tolist()))
    return freq

# solution [6]
def Solution6(lst):
    nums = [1,2,2,4,2,3,4,4,5,1]
    freq = pd.Series(nums).value_counts().to_dict()
    return freq


lst = [1,2,2,4,2,3,4,4,5,1]
print(Solution1(lst))
print(Solution2(lst))
print(Solution3(lst))
print(Solution4(lst))
print(Solution5(lst))
print(Solution6(lst))



######################  STRING  #########################
# input : s = "programming"
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# solution [1]
def Solution1(s):
    count_dict = Counter(s)
    return dict(count_dict)

# solution [2]
def Solution2(s):
    count_dict = {}

    for ch in s:
        if ch in count_dict:
            count_dict[ch] +=1
        else:
            count_dict[ch] = 1
    return count_dict

# solution [3]
def Solution3(s):
    return {ch: s.count(ch) for ch in set(s)}

# solution [4]
def Solution4(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


s = "programming"
print(Solution1(s))
print(Solution2(s))
print(Solution3(s))
print(Solution4(s))