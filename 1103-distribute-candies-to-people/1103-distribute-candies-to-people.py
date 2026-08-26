class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = num_people*[0]
        give = 0
        while candies>0:
            people[give%num_people] += min(candies,give+1)
            give+=1
            candies-=give

        return people

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna