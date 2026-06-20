class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for i in hm:
            if hm[i]==1:
                return i
        