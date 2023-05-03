#LeetCode Problem 1491. Average Salary Excluding the Minimum and Maximum Salary Solution
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary):
        for i in range(1, len(salary)):
            key = salary[i]
            j = i - 1
            while j >= 0 and salary[j] > key:
                salary[j + 1] = salary[j]
                j -= 1
            salary[j + 1] = key
        sum_salary = sum(salary) - salary[0] - salary[-1]
        num_employees = len(salary) - 2
        avg_salary = sum_salary / num_employees
        return avg_salary

salary = [4000,3000,1000,2000]
print(Solution().average(salary))