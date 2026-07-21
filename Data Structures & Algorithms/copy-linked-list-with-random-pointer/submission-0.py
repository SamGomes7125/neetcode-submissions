"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        current = head
        if current == None:
            return None
        while current:
            n = Node(current.val)
            dic[current] = n
            current = current.next
        current = head
        while current:
            copy = dic[current]
            if current.next == None:
                copy.next = None
            else:
                copy.next = dic[current.next]
            if current.random == None:
                copy.random = None
            else:
                copy.random = dic[current.random]
            current = current.next
        return dic[head]
        