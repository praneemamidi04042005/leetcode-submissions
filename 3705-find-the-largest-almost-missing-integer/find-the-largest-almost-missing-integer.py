class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hm={}
        if k==len(nums):
            return max(nums)
        for i in range(len(nums)-k+1):
            l=nums[i:i+k]
            for j in l:
                hm[j]=hm.get(j,0)+1
        m=-1
        for i in hm:
            if hm[i]==1:
                m=max(m,i)
        return m
        