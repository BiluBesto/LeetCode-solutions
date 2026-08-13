class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int targetSum = 0;
        for(int i=0;i<arr.size();i++)
        {
            targetSum+=arr[i];
        }
        if(targetSum!=0 && targetSum%3!=0)
        {
            return false;
        }
        int sum = targetSum/3;
        int ct = 0;
        int curSum = 0;
        for(int i=0;i<arr.size();i++)
        {
            curSum+=arr[i];
            if(curSum == sum)
            {
                curSum = 0;
                ct++;
            }
        }
        if(ct>=3)
        {
            return true;
        }
        return false;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna