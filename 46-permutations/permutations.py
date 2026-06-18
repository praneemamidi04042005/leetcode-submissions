class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutationHelper(index,s,res):
            if index==len(s):
                res.append(s[:])
                return
            for i in range(index,len(s)):
                s[i],s[index]=s[index],s[i] 
                permutationHelper(index+1,s,res)
                s[i],s[index]=s[index],s[i] 
        res=[]
        permutationHelper(0,nums,res)
        return res

        