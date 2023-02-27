#LeetCode Problem 436 - Find Right Interval Solution
#https://leetcode.com/problems/find-right-interval/

class Solution:      
    def findRightInterval(self, intervals):        
        if not intervals:
            return []
        elif len(intervals) == 1:
            return [-1]
        
        n = len(intervals)
        res = [-1] * n
        check_list = list(sorted([(i, val) for i, val in enumerate(intervals)], key=lambda x: x[1][0]))

        for i, interval in enumerate(intervals):
            value = interval[1]
            pos = self.binarySearch(check_list, value)
            if pos == n:
                continue
            else:
                res[i] = check_list[pos][0]

        return res
    
    def binarySearch(self, arr, value):
        start= 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) >> 1
            if arr[mid][1][0] < value:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
intervals = [[3,4],[2,3],[1,2]]
print(Solution().findRightInterval(intervals))