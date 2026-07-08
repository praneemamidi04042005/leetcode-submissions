class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxday=days[len(days)-1]
        dp=[]
        travelDay=[]
        for i in range(maxday+1):
            travelDay.append(False)
        for day in days:
            travelDay[day]=True
        for i in range(maxday+1):
            dp.append(0)
        for i in range(1,maxday+1):
            if not travelDay[i]:
                dp[i]=dp[i-1]
                continue
            dp[i]=costs[0]+dp[i-1]
            dp[i]=min(dp[max(0,i-7)]+costs[1],dp[i])
            dp[i]=min(dp[max(0,i-30)]+costs[2],dp[i])
        return dp[maxday]
        
        