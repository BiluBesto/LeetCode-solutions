class Solution {
public:
    bool check(vector<int>& nums) {
        int flag = 0;
        int prev=nums[0];
        for(int i:nums)
        {
            if(prev<=i)
            {
                prev=i;
            }
            else
            {
                prev=i;
                flag++;
            }
        }
        if(flag==1)
        {
            if(nums[0]>=nums[nums.size()-1])
                return true;
            else
                return false;
        }
        return flag<2;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna