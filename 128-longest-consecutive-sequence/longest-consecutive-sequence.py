class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if not nums:
            return 0
        c=1
        m=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                c+=1
            else:
                m=max(m,c)
                c=1
        m=max(m,c)
        return m
        