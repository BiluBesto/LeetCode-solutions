class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix or not matrix[0]:
            return False
        expected = deque(matrix[0])

        for i in range(1,len(matrix)):
            row = matrix[i]
            expected.pop()
            expected.appendleft(row[0])

            for j in range(1,len(row)):
                if row[j]!=expected[j]:
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna