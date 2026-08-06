class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> stor = {};
        vector<int> res[2];
        for(int i =0;i<nums.size();i++)
        {
            if(stor.count(target-nums[i]))
            {
                return {stor[target-nums[i]],i};
            }
            else
            {
                stor.insert({nums[i],i});
            }
        }
        return {};
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna