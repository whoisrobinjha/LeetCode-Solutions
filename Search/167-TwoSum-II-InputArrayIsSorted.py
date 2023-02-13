#Leetcode problem 167 - Two Sum II - Input Array Is Sorted solution
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1
        ans = [-1,-1]

        while(start < end):
            sum = numbers[start] +numbers[end]
            if(sum == target):
                ans[0] = start + 1
                ans[1] = end + 1
            if(sum < target):
                start += 1
            else:
                end -= 1
        return ans

numbers = [2,7,11,15]
target = 9

print(Solution().twoSum(numbers, target))