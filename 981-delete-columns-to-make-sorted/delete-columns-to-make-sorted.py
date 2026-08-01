class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        t=[]
        for i in range(len(strs[0])):
            p=[]
            for j in range(len(strs)):
                p.append(strs[j][i])
            t.append(p)
        for i in t:
            k=i[:]
            k.sort()
            if k!=i:
                c+=1
        return c


        