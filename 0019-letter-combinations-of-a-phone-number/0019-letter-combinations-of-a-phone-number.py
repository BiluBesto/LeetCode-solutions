class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        ph_mp = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        output = []
        def backtrack(combination,next_digits):
            if len(next_digits)==0:
                output.append(combination)
            else:
                for letter in ph_mp[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        backtrack("",digits)
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna