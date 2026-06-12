# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        p=head
        if head==None:
            return None
        while p:
            l.append(p.val)
            p=p.next
        k%=len(l)
        for i in range(k):
            t=l.pop()
            l.insert(0,t)
        p=head
        i=0
        while p:
            p.val=l[i]
            i+=1
            p=p.next
        return head
        