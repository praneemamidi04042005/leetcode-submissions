class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l=sentence.split()
        if len(l)==1:
            return l[0][0]==l[0][-1]
        for i in range(1,len(l)):
            if l[i][0]!=l[i-1][-1]:
                return False
        if l[len(l)-1][-1]!=l[0][0]:
            return False
        return True
