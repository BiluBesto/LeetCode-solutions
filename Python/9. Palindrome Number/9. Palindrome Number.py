class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        temp=x
        res=0
        while(temp!=0):
            res=res*10+(temp%10)
            temp=temp//10
        if(res==x):
            return True
        return False