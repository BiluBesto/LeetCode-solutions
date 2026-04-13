class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:
            return 0
        left = 0
        right = 0 
        m = 0
        c=0
        for i in range(len(s)):
            if s[i]=='(':
                left=left+1
            else:
                right=right+1
            if left==right:
                c=left+right
                m = max(m,c)
            elif left<right:
                left = 0 
                right=0
                c=0
        if m == len(s):
            return m
        left = 0
        right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='(':
                left=left+1
            else:
                right=right+1
            if left==right:
                c=left+right
                m=max(m,c)
            elif left>right:
                left=0
                right=0
                c=0
        return m