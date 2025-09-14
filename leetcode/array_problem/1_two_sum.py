# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


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