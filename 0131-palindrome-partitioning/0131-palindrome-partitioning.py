class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        def backtrack(start,path):
            if start==len(s):
                result.append(path)
                return
            for end in range(start+1,len(s)+1):
                if is_palindrome(s[start:end]):
                    backtrack(end,path + [s[start:end]])
        result = []
        backtrack(0,[])
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna