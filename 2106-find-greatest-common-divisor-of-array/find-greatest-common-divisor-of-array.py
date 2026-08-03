class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if a<b:
                a,b=b,a
            if a%b==0:
                return b
            return gcd(b,a%b)
        nums.sort()
        return gcd(nums[0],nums[-1])
        