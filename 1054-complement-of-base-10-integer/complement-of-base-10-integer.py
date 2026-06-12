class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)[2::]
        ss=''
        for i in s:
            if i=='0':
                ss+='1'
            else:
                ss+='0'
        return int(ss,2)