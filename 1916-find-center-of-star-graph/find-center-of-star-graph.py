class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hm={}
        for i in edges:
            for j in i:
                hm[j]=hm.get(j,0)+1
        for i in hm:
            if hm[i]==len(edges):
                return i