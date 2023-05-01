#LeetCode Problem 1365. How Many Numbers Are Smaller Than the Current Number Solution
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        count_dict = {}
        for num in sorted_nums:
            if num not in count_dict:
                count_dict[num] = sorted_nums.index(num)
        
        return [count_dict[num] for num in nums]
    
nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))