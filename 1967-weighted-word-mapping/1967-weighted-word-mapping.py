class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        map1 = {}
        res = ""
        for i in range(26):
            map1[i] = weights[i]
        map2 = {
            25:'a',24:'b',23:'c',22:'d',21:'e',20:'f', 19:'g',18:'h',17:'i',16:'j',15:'k',14:'l',
             13:'m',12:'n',11:'o',10:'p',9:'q',8:'r', 7:'s',6:'t',5:'u',4:'v',3:'w',2:'x',
             1:'y',0:'z'
        }
        for word in words:
            cur = 0
            for i in word:
                cur+=map1[ord(i)-ord('a')]
            cur%=26
            print(cur)
            res+=map2[cur]
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna