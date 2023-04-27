#Leetcode Problem 1346 - Check If N and Its Double Exist Solution
#https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr) -> bool:
        present = set()
        for x in arr:
            if 2 * x in present or (x % 2 == 0 and x // 2 in present):
                return True
            present.add(x)
        return False

arr = [3,1,7,11]
print(Solution().checkIfExist(arr))