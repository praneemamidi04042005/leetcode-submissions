class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        def gcd(a,b):
            if a<b:
                a,b=b,a
            if a%b==0:
                return b
            return gcd(b,a%b)
        return str1[:gcd(len(str1),len(str2))]

                
            
        