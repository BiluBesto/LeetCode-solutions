class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr = sentence.split(" ")

        new_str = ''
        count = 1

        for i in arr:
            if i[0] in 'aeiouAEIOU':
                str_temp = i + "ma" + "a" * count + " "
                new_str = new_str + str_temp
                count+=1
            else:
                str_temp = i[1:] + i[0] + "ma" + "a"*count + " "
                new_str = new_str + str_temp
                count+=1
        return new_str.rstrip()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna