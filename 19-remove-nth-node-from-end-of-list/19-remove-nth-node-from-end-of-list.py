# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        pre = (count - n)
        
        node = dummy
        for _ in range(pre):
            node = node.next
        
        node.next = node.next.next
        
        return dummy.next