# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        n2 = []
        result = []
        c = 0
        current1 = l1
        current2 = l2
        while current1 or current2:
            if not current1:
                n1.append(0)
            else:
                n1.append(current1.val)
            if not current2:
                n2.append(0)
            else:
                n2.append(current2.val)
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
        for i in range(len(n1)):
            if n1[i]+n2[i]+c < 10:
                result.append(n1[i]+n2[i]+c)
                c = 0
            else:
                result.append((n1[i]+n2[i]+c) - 10)
                c = 1
        if c == 1:
            result.append(1)
        result_list = ListNode(0)
        tail = result_list
        for i in range(len(result)):
            new_node = ListNode(result[i])
            tail.next = new_node
            tail = tail.next
        return result_list.next

        

            



        