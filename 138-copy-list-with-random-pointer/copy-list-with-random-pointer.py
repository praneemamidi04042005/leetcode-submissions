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
        p=head
        hm={}
        while p:
            newnode=Node(p.val)
            hm[p]=newnode
            p=p.next
        hm[None]=None
        p=head
        while p:
            copynode=hm[p]
            copynode.next=hm[p.next]
            copynode.random=hm[p.random]
            p=p.next
        return hm[head]
        