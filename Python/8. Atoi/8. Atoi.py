class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "":
            return 0
        res = ""
        sign = 1
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for i in s:
            if i.isdigit():
                if not (res == "" and i == "0"):
                    res += i
            else:
                break
        if res == "":
            return 0
        if sign * int(res) < -2 ** 31:
            return -2 ** 31
        elif (sign * int(res) > 2 ** 31 - 1):
            return 2 ** 31 - 1
        return sign * int(res)
