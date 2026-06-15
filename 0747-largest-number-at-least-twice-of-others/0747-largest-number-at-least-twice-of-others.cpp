class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int max = 0;
        int maxi = -1;
        for(int i =0;i<nums.size();i++)
        {
            if(max<nums[i])
            {
                max = nums[i];
                maxi = i;
            }
        }
        for(int i =0;i<nums.size();i++)
        {
            if(nums[i]==max)
                continue;
            if(2*nums[i]>max)
                return -1;
        }
        return maxi;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna