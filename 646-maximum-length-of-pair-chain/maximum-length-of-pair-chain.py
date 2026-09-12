class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        
        current_end = float('-inf')
        count = 0
        for p in pairs:
            # If the start of the current pair is greater than the last end
            if p[0] > current_end:
                current_end = p[1]
                count += 1
        return count