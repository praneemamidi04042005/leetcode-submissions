class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s+=nums[i]
        m=s
        for i in range(k,len(nums)):
            s-=nums[i-k]
            s+=nums[i]
            m=max(s,m)
        return float("%.5f"%(m/k))

        