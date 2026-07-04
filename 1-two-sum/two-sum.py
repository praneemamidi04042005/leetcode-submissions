class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in seen:
                return [nums.index(compliment),i]
            seen.add(nums[i])
        