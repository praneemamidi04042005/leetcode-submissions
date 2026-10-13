class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        s=0
        l=[]
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]*=-1
        nums.sort()
        l=sum(i*i for i in nums[0:len(nums)//2])
        s=sum(i*i for i in nums[len(nums)//2:])
        return s-l

        