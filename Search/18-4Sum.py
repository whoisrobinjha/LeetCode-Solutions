#LeetCode Problem 18 - 4Sum Solution
# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        result = set()
        
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return list(result)

nums = [1,0,-1,0,-2,2]
target = 0
print(Solution().fourSum(nums, target))