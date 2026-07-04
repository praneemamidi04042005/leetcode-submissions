class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm={}
        for i in range(len(s)):
            if s[i] not in hm:  
                hm[s[i]]=t[i]
            else:
                if hm[s[i]]!=t[i]:
                    return False
        hm1={}
        for i in range(len(s)):
            if t[i] not in hm1:  
                hm1[t[i]]=s[i]
            else:
                if hm1[t[i]]!=s[i]:
                    return False
        
        return True
        