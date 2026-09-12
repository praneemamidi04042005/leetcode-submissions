class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = []

        for _, h in envelopes:
            left = 0
            right = len(tails)

            # Lower Bound
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < h:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tails):
                tails.append(h)
            else:
                tails[left] = h
        return len(tails)