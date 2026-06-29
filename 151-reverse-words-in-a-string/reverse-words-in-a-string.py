class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        l=s.split(" ")[::-1]
        ss=''
        for i in range(len(l)):
            l[i]=l[i].strip()
            if l[i]!='':
                ss+=l[i]
                ss+=' '
        return ss[:len(ss)-1]
        