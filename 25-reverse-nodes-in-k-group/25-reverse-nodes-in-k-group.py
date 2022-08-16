# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previousGroup = dummy   # END of previous group
        
        while True:
            kth = self.findKth(previousGroup, k)
            if not kth:
                break   # Can't reverse <k sublist
            
            nextGroup = kth.next    # START of next group
            # After reversal, end points to next group, so
            # Previous can be set to head of nextGroup
            prev, curr = nextGroup, previousGroup.next
            
            # Stay within the k-group, do reversal
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Connect the last group to the current
            # And update previous group
            tmp = previousGroup.next
            previousGroup.next = kth 
            previousGroup = tmp
        
        return dummy.next
            
            
            
            