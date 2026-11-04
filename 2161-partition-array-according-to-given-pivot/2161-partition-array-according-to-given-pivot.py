class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        frpiv = 0
        for i in nums:
            if i == pivot:
                frpiv+=1
        l = []
        r = []
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i>pivot:
                r.append(i)
        res = l
        for i in range(frpiv):
            res.append(pivot)
        res.extend(r)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna