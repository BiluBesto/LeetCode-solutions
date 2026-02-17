class Solution(object):
    def isNumber(self, s):
        decimal_seen = False
        decimal_sign = False
        seenE = False
        digit_seen = False
        firstDot = False
        i=0
        if s[i] in ['+','-']:
            i+=1
        elif s[i].isalpha():
            return False
        while i<len(s):
            if s[i] in ['1','2','3','4','5','6','7','8','9','0'] and seenE:
                decimal_seen = True
            elif s[i] in ['1','2','3','4','5','6','7','8','9','0'] and not decimal_seen:
                digit_seen = True
            elif not seenE and s[i]=='.' and not firstDot:
                firstDot = True
            elif seenE and s[i] in ['+','-'] and not decimal_seen and not decimal_sign:
                decimal_sign = True
            elif s[i] in ['e','E'] and not seenE and digit_seen:
                seenE = True
            else:
                return False
            i+=1

        print(digit_seen)
        print(seenE)
        if seenE:
            return decimal_seen and digit_seen
        else:
            return digit_seen
        