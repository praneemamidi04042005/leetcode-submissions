class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        c=0
        while x>=1 and y>=4:
            x-=1
            c+=1
            y-=4
        if c%2==1:
            return "Alice"
        else:
            return "Bob"

        