class Solution:
    def minimumPushes(self,A) -> int:
        q, r = divmod(len(A), 8)
        return ((q << 2) + r) * (q + 1)
        