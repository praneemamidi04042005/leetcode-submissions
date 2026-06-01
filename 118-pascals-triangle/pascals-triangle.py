class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        def generateRow(row):
            ansRow=[]
            ans=1
            ansRow.append(1)
            for col in range(1,row):
                ans*=(row-col)
                ans//=col
                ansRow.append(ans)
            return ansRow
        for i in range(1,numRows+1):
            res.append(generateRow(i))
        return res
                
