class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        c=0
        for i in range(len(l)):
            b=False
            for j in range(len(l[i])):
                if l[i][j] in brokenLetters:
                    b=True
            if not b:
                c+=1
        return c
        