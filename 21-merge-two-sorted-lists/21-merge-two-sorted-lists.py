# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        dummy = ListNode(0, list1)
        
        curNode = dummy
        while list1 and list2:
            if list2.val <= list1.val:
                curNode.next = list2
                list2 = list2.next
            else:
                curNode.next = list1
                list1 = list1.next
            
            curNode = curNode.next
        
        if list1:
            curNode.next = list1
        elif list2:
            curNode.next = list2
        
        return dummy.next
    