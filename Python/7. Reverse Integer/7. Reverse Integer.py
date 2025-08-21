class Solution:
    def reverse(self, x: int) -> int:
        temp=0
        rev=0
        if(x<0):
            temp=abs(x)
        else:
            temp=x
        while(temp!=0):
            rev=rev*10+temp%10
            temp=temp//10
        if(x<0):
            rev= -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        else:
            return rev