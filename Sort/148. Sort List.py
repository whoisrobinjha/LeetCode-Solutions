#LeetCode Problem 148. Sort List Solution
# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        gap = length // 2
        while gap > 0:
            for i in range(gap, length):
                curr = head
                for _ in range(i):
                    curr = curr.next
                key = curr.val
                prev = curr
                curr = curr.next
                while curr and curr.val > key:
                    prev.val = curr.val
                    prev = prev.next
                    curr = curr.next
                prev.val = key
            gap //= 2

        return head