class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int prev = nums[0];
        for(int i =1;i<nums.size();i++)
        {
            if(prev==nums[i])
            {
                nums.erase(nums.begin()+i);
                i--;
            }
            else
            {
                prev = nums[i];
            }
        }
        return nums.size();
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna