class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=0
        for i in range(len(s)):
            ss=''
            for j in range(i,len(s)):
                ss+=s[j]
                if ss==ss[::-1]:
                    m=max(len(ss),m)
        for i in range(len(s)):
            ss=''
            for j in range(i,len(s)):
                ss+=s[j]
                if ss==ss[::-1] and m==len(ss):
                    return ss