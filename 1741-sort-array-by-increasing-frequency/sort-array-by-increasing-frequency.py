class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        l=[]
        for i in hm:
            l.append((hm[i],-i))
        l.sort()
        p=[]
        for i in range(len(l)):
            for j in range(hm[-l[i][1]]):
                p.append(-l[i][1])
        return p

        

        