# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #naive approach with set
        s1 = set()
        while head:
            if head in s1:
                return True
            if head not in s1:
                s1.add(head)
                head = head.next
        return False