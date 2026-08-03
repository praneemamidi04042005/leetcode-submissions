class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b1=bin(start)[2::]
        b2=bin(goal)[2::]
        if len(b1)<len(b2):
            for i in range(len(b2)-len(b1)):
                b1='0'+b1
        if len(b2)<len(b1):
            for i in range(len(b1)-len(b2)):
                b2='0'+b2
        c=0
        for i in range(len(b1)):
            if b1[i]!=b2[i]:
                c+=1
        return c
        
        