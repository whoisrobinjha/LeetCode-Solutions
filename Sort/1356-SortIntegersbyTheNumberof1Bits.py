#LeetCode Problem 1356 - Sort Integers by The Number of 1 Bits Solution
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr):
        count_dict = {}
        for num in arr:
            count = bin(num).count('1')
            if count in count_dict:
                count_dict[count].append(num)
            else:
                count_dict[count] = [num]
        sorted_dict = self.sort_dict_by_count(count_dict)
        sorted_arr = []
        for count, nums in sorted_dict:
            nums.sort()
            sorted_arr.extend(nums)
        return sorted_arr

    def sort_dict_by_count(self, count_dict):
        return sorted(count_dict.items())

arr = [0,1,2,3,4,5,6,7,8]
print(Solution().sortByBits(arr))