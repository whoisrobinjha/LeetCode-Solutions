#LeetCode Problem 1470 - Shuffle the Array Solution
#https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result
    
nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums, n))