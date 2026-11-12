class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m=0
        for i in range(len(nums)):
            c=0
            j=i
            while j+1 in range(len(nums)) and nums[j]<nums[j+1]:
                c+=1
                j+=1
            m=max(m,c)
        for i in range(len(nums)):
            c=0
            j=i
            while j+1 in range(len(nums)) and nums[j]>nums[j+1]:
                c+=1
                j+=1
            m=max(m,c)
        return m+1
        

        