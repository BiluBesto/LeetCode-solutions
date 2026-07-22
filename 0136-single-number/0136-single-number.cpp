class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res=nums[0];
        for(int i = 1; i< nums.size();i++)
        {
            res^=nums[i];
        }
        return res;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna