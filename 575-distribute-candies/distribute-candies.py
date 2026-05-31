class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c=0
        l=list(set(candyType))
        if len(l)<=len(candyType)//2:
            c+=len(l)
        else:
            c+=len(candyType)//2
        return c
        