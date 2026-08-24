class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j],matrix[i][len(matrix[0])-j-1] = matrix[i][len(matrix[0])-j-1], matrix[i][j]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna