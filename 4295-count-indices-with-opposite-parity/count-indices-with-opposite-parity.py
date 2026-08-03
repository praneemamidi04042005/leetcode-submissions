class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            c=0
            for j in range(i+1,len(nums)):
                if nums[i]%2==0 and nums[j]%2==1:
                    c+=1
                if nums[i]%2==1 and nums[j]%2==0:
                    c+=1
            nums[i]=c
        return nums


        