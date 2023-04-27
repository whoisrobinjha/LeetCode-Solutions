#LeetCode Problem 1095 - Find in Mountain Array Solution
# https://leetcode.com/problems/find-in-mountain-array/

class Solution:
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = peak, n - 1
        while l <= r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                r = mid - 1
            else:
                l = mid + 1

        return -1