#LeetCode Problem 832 - Flipping an Image Solution
#https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)
        for i in range(n):
            image[i] = image[i][::-1]
            for j in range(n):
                image[i][j] = 1 - image[i][j]
        return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))