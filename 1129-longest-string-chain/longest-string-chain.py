class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        res=0
        dp={}
        for word in words:
            dp[word]=1
            for i in range(len(word)):
                pre=word[:i]+word[i+1:] 
                if pre in dp:
                    dp[word]=max(dp[word],dp[pre]+1)
            res=max(res,dp[word])
        return res       