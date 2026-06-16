class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds=[]
        ansList=[]
        def findSubsets(ind,nums):
            ansList.append(ds[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                findSubsets(i+1,nums)
                ds.remove(ds[len(ds)-1])
        nums.sort()
        findSubsets(0,nums)
        return ansList
        