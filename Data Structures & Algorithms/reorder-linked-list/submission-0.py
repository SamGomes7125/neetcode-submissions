# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current1 = head
        current2 = head
        prev_node = None
        while current2 and current2.next:
            current1 = current1.next
            current2 = current2.next.next
        second_half = current1.next
        current1.next = None
        while second_half:
            c = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = c
        current1 = head
        second_half = prev_node
        while second_half:
            c1 = second_half
            n1 = second_half.next
            n2 = current1.next
            current1.next = c1
            current1.next.next = n2
            second_half = n1
            current1 = n2


            

        