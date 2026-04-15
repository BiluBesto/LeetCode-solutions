from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        has_odd = False
        length= 0
        for c in count.values():
            length += (c//2)*2
            if c%2==1:
                has_odd = True
        
        return length + (1 if has_odd else 0)