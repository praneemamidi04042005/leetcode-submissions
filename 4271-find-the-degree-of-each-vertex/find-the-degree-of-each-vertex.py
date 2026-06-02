class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        l=[]
        for i in matrix:
            l.append(sum(i))
        return l
        