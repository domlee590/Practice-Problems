# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Create a dummy node for edge case that reversal starts at 1
        dummy = ListNode(0, head)
        
        #First get pointers to before and start of reversed segment
        before, cur = dummy, head
        for _ in range(left - 1):
            before, cur = cur, cur.next
            
        #Reverse the inner linked list
        prev = None
        for _ in range((right - left) + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        #Connect the end of the reversed list
        before.next.next = cur
        
        #Connect the beginning of the reversed list
        before.next = prev
        
        #Return the new head (head may have been changed in reversal)
        return dummy.next