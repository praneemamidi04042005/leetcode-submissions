class Solution:
    def findTargetSumWays(self, nums, target):
        total=sum(nums)
        if abs(target)>total:
            return 0
        n=len(nums)
        dp=[[0]*(2*total+1) for _ in range(n+1)]
        dp[0][total]=1
        for i in range(1,n+1):
            for j in range(2*total+1):
                if dp[i-1][j]!=0:
                    dp[i][j+nums[i-1]]+=dp[i-1][j]
                    dp[i][j-nums[i-1]]+=dp[i-1][j]
        return dp[n][target+total]