#LeetCode Problem 1365 - How Many Numbers Are Smaller Than the Current Number Solution
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        result = []
        for num in nums:
            count = 0
            for smaller_num in counts:
                if smaller_num < num:
                    count += counts[smaller_num]
            result.append(count)
        return result
    
nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))