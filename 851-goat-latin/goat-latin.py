class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l=sentence.split()
        for i in range(len(l)):
            s=''
            if l[i][0] in 'aeiouAEIOU':
                s+=l[i]
            else:
                s+=l[i][1:]
                s+=l[i][0]
            s+='ma'
            s+='a'*(i+1)
            l[i]=s
        return ' '.join(l)

        