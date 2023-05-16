#LeetCode Problem 147. Insertion Sort List Solution
# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        
        sorted_head = ListNode(float('-inf'))
        sorted_tail = sorted_head
        
        while head:
            curr = head
            head = head.next
            
            if curr.val < sorted_tail.val:
                sorted_tail = sorted_head
            
            while sorted_tail.next and curr.val > sorted_tail.next.val:
                sorted_tail = sorted_tail.next
            
            curr.next = sorted_tail.next
            sorted_tail.next = curr
            
        return sorted_head.next