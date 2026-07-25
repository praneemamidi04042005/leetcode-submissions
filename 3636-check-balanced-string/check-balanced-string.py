class Solution:
    def isBalanced(self, num: str) -> bool:
        s1=0
        s2=0
        for i in range(0,len(num),2):
            s1+=ord(num[i])-48
            
        for i in range(1,len(num),2):
            s2+=ord(num[i])-48


        print(s1,s2)
        return s1==s2
        