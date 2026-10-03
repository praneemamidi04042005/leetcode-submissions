class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base10_to_any(n, base):
            if n == 0:
                return "0"
            
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            
            while n > 0:
                result = digits[n % base] + result
                n //= base
                
            return result
        for i in range(2,n-1):
            s=base10_to_any(n,i)
            if s!=s[::-1]:
                return False
        return True
        