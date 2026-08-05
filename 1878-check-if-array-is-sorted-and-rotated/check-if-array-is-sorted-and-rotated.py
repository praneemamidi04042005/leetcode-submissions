class Solution:
    def check(self, nums: List[int]) -> bool:
        fault=False
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                if fault:
                    return False
                fault=True
        return True
        