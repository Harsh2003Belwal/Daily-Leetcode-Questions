class Solution:
    def reverseWords(self, s: str) -> str:
        b=[]
        a=s.split()
        b=a[::-1]
        return " ".join(b)
            
        