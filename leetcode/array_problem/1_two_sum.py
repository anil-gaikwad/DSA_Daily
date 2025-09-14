# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# 2. Hash Map Approach

def two_sum(nums, target):
    maps = {}

    for idx, num in enumerate(nums):
        compliment = target - num
        if compliment in maps:
            return [maps[compliment], idx]
        maps[ num] = idx
    return []


nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))


# Time Complexity: O(n)
# Space Complexity: O(n)

#-----------------------------------------------#
# 2. Brute Force Approach
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [2,7,11,15]
target = 9
print(two_sum_brute_force(nums, target))


# Time Complexity: O(n^2)
# Space Complexity: O(1)