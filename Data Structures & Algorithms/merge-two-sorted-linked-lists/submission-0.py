# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        dummy = ListNode(0)  # A fake starting point
        tail = dummy
        while current1 and current2:
            if current1.val <= current2.val:
                tail.next = current1
                current1 = current1.next
            elif current2.val < current1.val:
                tail.next = current2
                current2 = current2.next
            tail = tail.next
        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2   
        return dummy.next
