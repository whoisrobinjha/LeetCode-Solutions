#LeetCode Problem 1491. Average Salary Excluding the Minimum and Maximum Salary Solution
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary):
        self.insertion_sort(salary)
        total_sum = sum(salary[1:-1])
        average = total_sum / (len(salary) - 2)
        return average
        
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
salary = [4000,3000,1000,2000]
print(Solution().average(salary))