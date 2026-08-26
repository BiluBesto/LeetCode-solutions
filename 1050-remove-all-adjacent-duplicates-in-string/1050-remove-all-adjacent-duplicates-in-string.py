class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ch in s:
            if st and ch == st[-1]:
                st.pop()
            else:
                st.append(ch)
        return "".join(st)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna