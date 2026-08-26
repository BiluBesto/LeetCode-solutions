class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_characters(s):
            stack = []

            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char!='#':
                    stack.append(char)
            return stack
        return remove_characters(s)==remove_characters(t)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna