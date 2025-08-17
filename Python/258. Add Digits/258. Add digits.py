import math
class Solution:
    def addDigits(self, num: int) -> int:
        while(num//10!=0):
            c=0
            while(num!=0):
                c=c+num%10
                num=num//10
            num=c
        return num
