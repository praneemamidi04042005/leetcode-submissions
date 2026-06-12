class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        hm={}
        for i in range(97,123):
            hm[chr(i)]=i-97
        s1=0
        s2=0
        for i in firstWord:
            s1=s1*10+hm[i]
        for i in secondWord:
            s2=s2*10+hm[i]
        t=0
        for i in targetWord:
            t=t*10+hm[i]
        return s1+s2==t


        