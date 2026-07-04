class Solution:
    def isValid(self, s: str) -> bool:

        st=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                else:
                    top=st[-1]
                    if top=='(' and i==')':
                        st.pop()
                    elif top=='[' and i==']':
                        st.pop()
                    elif top=='{' and i=='}':
                        st.pop()
                    else:
                        return False
        return len(st)==0
                    