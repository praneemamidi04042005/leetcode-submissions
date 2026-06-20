class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)[2::]
        if '11' in b or '00' in b:
            return False
        return True
        