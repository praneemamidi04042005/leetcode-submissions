class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum_area=0
        left=0
        right=len(height)-1
        while left<right:
            maximum_area=max(maximum_area,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maximum_area
        