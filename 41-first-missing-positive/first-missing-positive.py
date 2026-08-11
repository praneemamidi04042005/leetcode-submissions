class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for i in range(1,len(nums)+1):
            if i not in hm:
                return i
        return len(nums)+1
        