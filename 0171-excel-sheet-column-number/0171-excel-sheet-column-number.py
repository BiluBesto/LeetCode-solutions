class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lookup = {}
        lookup['A'] = 1
        lookup['B'] = 2
        lookup['C'] = 3
        lookup['D'] = 4
        lookup['E'] = 5
        lookup['F'] = 6
        lookup['G'] = 7
        lookup['H'] = 8
        lookup['I'] = 9
        lookup['J'] = 10
        lookup['K'] = 11
        lookup['L'] = 12
        lookup['M'] = 13
        lookup['N'] = 14
        lookup['O'] = 15
        lookup['P'] = 16
        lookup['Q'] = 17
        lookup['R'] = 18
        lookup['S'] = 19
        lookup['T'] = 20
        lookup['U'] = 21
        lookup['V'] = 22
        lookup['W'] = 23
        lookup['X'] = 24
        lookup['Y'] = 25
        lookup['Z'] = 26
        ans = 0
        x = 0
        for i in columnTitle[::-1]:
            ans = ans + (26**x)*lookup[i]
            x+=1
        return ans
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna