class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def permutationHelper( s, index, res):
            if index == len(s):
                res.append("".join(s))
                return
            for i in range(index, len(s)):
                # Swap and recurse
                s[i], s[index] = s[index], s[i]
                permutationHelper(s, index + 1, res)
                s[i], s[index] = s[index], s[i]  # backtrack
        s = [str(i + 1) for i in range(n)]
        res = []
        permutationHelper(s, 0, res)  # Generate all permutations
        res.sort()  # Sort the generated permutations
        
        # Make k 0-based indexed to point to kth sequence
        return res[k - 1]