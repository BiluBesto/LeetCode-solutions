class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int counter[26] = {0};
        for(char ch : magazine)
            counter[ch-'a']++;
        for(char ch : ransomNote)
        {
            if(counter[ch-'a']-- <=0)
            {
                return false;
            }
        }
        return true;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna