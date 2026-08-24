class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target_sum=sum(nums)//2
        dp=[]
        n=len(nums)
        for i in range(n+1):
            k=[]
            for j in range(target_sum+1):
                k.append(False)
            dp.append(k)
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,target_sum+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][target_sum]

      