from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            return 0
        l=[]
        for i in nums:
            l.append(str(i))
        l.sort(key=cmp_to_key(compare))
        ans="".join(l)
        if ans[0]=='0':
            return '0'
        return "".join(l)