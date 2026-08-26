class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False

        if A==B:
            return True if len(A) - len(set(A))>=1 else False
        
        diff = []
        for i in range(len(A)):
            if A[i]!=B[i]:
                diff.append(i)
                if len(diff)>2:
                    return False
        if len(diff)!=2:
            return False
        
        if A[diff[0]] == B[diff[1]] and B[diff[0]] == A[diff[1]]:
            return True
    

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna