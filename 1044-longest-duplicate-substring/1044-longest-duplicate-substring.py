class Solution:
    def RabinKarp(self,text,mid,q):
        if mid == 0: 
            return True
        h,t,d = (1<<(8*mid-8))%q ,0 ,256
        dict = defaultdict(list)

        for i in range(mid):
            t = (d*t + ord(text[i]))%q
            dict[t].append(i-mid+1)
        
        for i in range(len(text)-mid):
            t = (d*(t-ord(text[i])*h)+ ord(text[i+mid]))%q
            for j in dict[t]:
                if text[i+1:i+mid+1]==text[j:j+mid]:
                    return (True, text[j:j+mid])
            dict[t].append(i+1)
        return (False, "")
    def longestDupSubstring(self, s: str) -> str:
        res = ""
        beg, end = 0, len(s)
        q = (1<<31) - 1

        while beg+1<end:
            mid = (beg+end)//2
            isFound, candidate = self.RabinKarp(s,mid,q)
            if isFound:
                beg, res = mid, candidate
            else:
                end = mid


        return res