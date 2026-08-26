class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        tx , ty = 0,0
        for i in range(0,len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='R':
                    tx,ty = i,j
        
        count = 0
        left , top = False,False
        ch1,ch2 = True, True
        for i in range(0,8):
            if i < tx:
                if board[i][ty]=='p':
                    top = True
                elif board[i][ty]=='B':
                    top = False
            elif i>tx:
                if board[i][ty] =='p' and ch1:
                    ch1 = False
                    count+=1
                elif board[i][ty] == 'B':
                    ch1= False
            if i<ty:
                if board[tx][i] == 'p':
                    left = True
                elif board[tx][i] == 'B':
                    left = False
            elif i>ty:
                if board[tx][i] == 'p' and ch2:
                    ch2 = False
                    count+=1
                elif board[tx][i]=='B':
                    ch2 = False
        if left:
            count+=1
        if top:
            count+=1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna