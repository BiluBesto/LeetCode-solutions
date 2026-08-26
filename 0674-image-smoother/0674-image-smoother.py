class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img),len(img[0])

        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = self.smoothen(img,i,j)
        
        return res

    def smoothen(self, img, x, y):
        m,n = len(img),len(img[0])
        sum,count = 0,0

        for i in range(-1,2):
            for j in range(-1,2):
                nx , ny = x+i, y+j
                if 0<=nx < m and 0 <= ny <n:
                    sum+=img[nx][ny]
                    count+=1
        return sum//count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna