class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hm={}
        ch=97
        for i in key:
            if i not in hm and i!=' ':
                hm[i]=chr(ch)
                ch+=1
        s=''
        for i in message:
            if i==' ':
                s+=i
            else:
                s+=hm[i]
        return s
        