class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=float('-inf')
        pref=1
        suff=1
        for i in range(len(nums)):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[len(nums)-i-1]
            m=max(m,max(pref,suff))
        return m
        