class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        def findCombinations(ind,arr,target):
            if target==0:
                ans.append(ds[:])
                return
            for i in range(ind,len(arr)):
                if i!=ind and arr[i]==arr[i-1]:
                    continue
                if arr[i]>target:
                    break
                ds.append(arr[i])
                findCombinations(i+1,arr,target-arr[i])
                ds.remove(ds[len(ds)-1])
        candidates.sort()
        findCombinations(0,candidates,target)
        return ans
        