class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s=sum(apple)
        i=0
        while s!=0:
            if capacity[i]!=0:
                capacity[i]-=1
                s-=1
            else:
                i+=1
        return i+1
        
