#LeetCode Problem 1773. Count Items Matching a Rule Solution
# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                count += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                count += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                count += 1
        return count

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(Solution().countMatches(items, ruleKey, ruleValue))
