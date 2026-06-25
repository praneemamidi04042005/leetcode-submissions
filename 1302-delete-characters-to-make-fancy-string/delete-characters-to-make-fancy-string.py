class Solution:
    def makeFancyString(self, s: str) -> str:
        l=''
        for i in s:
            if len(l)<2:
                l+=i
            else:
                if i==l[-1] and i==l[-2]:
                    continue
                else:
                    l+=i
        return l
        