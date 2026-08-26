class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {}
        map_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for i in range(97,123):
            dic[chr(i)] = map_morse[i-97]
        diff = []

        for w in words:
            cur = ""
            for x in w:
                cur+= dic[x]
            if cur not in diff:
                diff.append(cur)
        return len(diff)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna