class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pl=[]
        nl=[]
        for i in nums:
            if i>0:
                pl.append(i)
            else:
                nl.append(i)
        for i in range(0,len(nums),2):
            nums[i]=pl[i//2]
            nums[i+1]=nl[i//2]
        return nums
        