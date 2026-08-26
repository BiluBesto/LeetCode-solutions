class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        word_count = {}
        i,n = 0,len(paragraph)

        while i<n:
            while i<n and not paragraph[i].isalpha():
                i+=1
            temp = []
            while i<n and paragraph[i].isalpha():
                temp.append(paragraph[i].lower())
                i+=1
            word = "".join(temp)
            if word and word not in banned_set:
                word_count[word] = word_count.get(word,0)+1
        max_word = ""
        max_freq = 0
        for w,f in word_count.items():
            if f>max_freq:
                max_freq = f
                max_word = w 

        return max_word

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna