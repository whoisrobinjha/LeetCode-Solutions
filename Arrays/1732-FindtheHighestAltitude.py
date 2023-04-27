#Leetcode Problem 1732 - Find the Highest Altitude Solution
#https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain):
        max_altitude = 0
        altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude
    
gain = [-5,1,5,0,-7]
print(Solution().largestAltitude(gain))