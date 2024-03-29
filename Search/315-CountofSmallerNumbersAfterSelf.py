#LeetCode Problem 315 - Count of Smaller Numbers After Self Solution
#https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
    
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

nums = [5,2,6,1]
print(Solution().countSmaller(nums))