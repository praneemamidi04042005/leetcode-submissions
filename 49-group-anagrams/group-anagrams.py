class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        k=[]
        for i in strs:
            l=list(i)
            l.sort()
            s=''.join(l)
            if s not in hm:
                hm[s]=[]
            hm[s].append(i)
        for i in hm:
            k.append(hm[i])
        return k