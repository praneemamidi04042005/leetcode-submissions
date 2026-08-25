class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        st=''
        n=len(str1)
        m=len(str2)
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        i=n
        j=m
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                st=str1[i-1]+st
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    st=str2[j-1]+st
                    j-=1
                else:
                    st=str1[i-1]+st
                    i-=1     
        while i > 0:
            st = str1[i-1] + st
            i -= 1
        while j > 0:
            st = str2[j-1] + st
            j -= 1   
        return st