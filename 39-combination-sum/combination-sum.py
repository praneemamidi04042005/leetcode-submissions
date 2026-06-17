class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        def findCombinations(ind,arr,target):
            if ind==len(arr):
                if target==0:
                    ans.append(ds[:])
                return
            if arr[ind]<=target:
                ds.append(arr[ind])
                findCombinations(ind,arr,target-arr[ind])
                ds.remove(ds[len(ds)-1])
            findCombinations(ind+1,arr,target)
        findCombinations(0,candidates,target)
        return ans