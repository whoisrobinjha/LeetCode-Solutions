#LeetCode Problem 1854 - Maximum Population Year Solution
#https://leetcode.com/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs):
        population = {}
        for birth, death in logs:
            for year in range(birth, death):
                if year not in population:
                    population[year] = 0
                population[year] += 1
        max_population = max(population.values())
        earliest_year = float('inf')
        for year, count in population.items():
            if count == max_population and year < earliest_year:
                earliest_year = year
        return earliest_year

logs = [[1993,1999],[2000,2010]]
print(Solution().maximumPopulation(logs))