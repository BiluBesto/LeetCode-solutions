class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.','')
            seen.add(local+'@'+domain)
        return len(seen)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna