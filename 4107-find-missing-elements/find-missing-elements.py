class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                l.append(i)
        return l
        