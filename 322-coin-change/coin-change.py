class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def find(ind,t,coins,dp):
            if ind==0:
                if t%coins[ind]==0:
                    return t//coins[ind]
                else:
                    return float('inf')
            if dp[ind][t]!=-1:
                return dp[ind][t]
            nottake=find(ind-1,t,coins,dp)
            take=float('inf')
            if coins[ind]<=t:
                take=1+find(ind,t-coins[ind],coins,dp)
            
            dp[ind][t]=min(take,nottake)
            return dp[ind][t]
        dp=[]
        for i in range(len(coins)):
            k=[]
            for j in range(amount+1):
                k.append(-1)
            dp.append(k)
        ans=find(len(coins)-1,amount,coins,dp)
        if ans!=float('inf'):
            return ans
        else:
            return -1
        