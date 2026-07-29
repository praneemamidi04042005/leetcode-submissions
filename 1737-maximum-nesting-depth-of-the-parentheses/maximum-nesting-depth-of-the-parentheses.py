class Solution:
    def maxDepth(self, s: str) -> int:
        ss=[]
        m=0
        for i in s:
            if i=='(':
                ss.append(i)
                m=max(m,len(ss))
            elif i==')':
                ss.pop()
        return m
        