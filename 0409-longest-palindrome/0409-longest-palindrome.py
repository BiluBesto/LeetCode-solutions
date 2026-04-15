from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        
        for c in count.values():
            length += (c // 2) * 2
            if c % 2 == 1:
                odd_found = True
        
        return length + (1 if odd_found else 0)