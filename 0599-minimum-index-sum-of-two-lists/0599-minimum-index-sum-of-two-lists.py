class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = float('inf')
        ans = ""
        for i in range(len(list1)):
            if list1[i] in list2: 
                if m>list2.index(list1[i])+i:
                    ans = [list1[i]]
                    m = min(m,list2.index(list1[i])+i)
                elif m==list2.index(list1[i])+i:
                    ans.append(list1[i])
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna