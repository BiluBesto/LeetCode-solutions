class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int rightSum = accumulate(nums.begin(),nums.end(),0);

        int leftSum = 0 ;

        for(int i = 0;i<nums.size();i++)
        {
            rightSum -=nums[i];
            if(leftSum == rightSum)
                return i;
            leftSum +=nums[i];
        }
        return -1;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna