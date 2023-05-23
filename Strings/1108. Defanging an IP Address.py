#LeetCode Problem 1108. Defanging an IP Address Solution
# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_address = ""
        for char in address:
            if char == ".":
                defanged_address += "[.]"
            else:
                defanged_address += char
        return defanged_address

address = "1.1.1.1"
print(Solution().defangIPaddr(address))