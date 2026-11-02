class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        if n%2==0:
            k=math.floor((nums[n//2]+nums[n//2-1])/2)
        else:
            k=nums[n//2]
        s=0
        for i in nums:
            s+=abs(i-k)
        return s
        