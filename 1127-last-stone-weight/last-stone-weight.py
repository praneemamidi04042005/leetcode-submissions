class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)!=1:
            stones.sort()
            p=stones.pop()
            k=stones.pop()
            stones.append(abs(p-k))
        return stones[0]
        