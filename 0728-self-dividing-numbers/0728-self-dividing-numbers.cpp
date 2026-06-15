class Solution {
public:
    bool helper(int x)
    {
        int temp  = x;
        while(x>0)
        {
            if(x%10==0||temp%(x%10)!=0)
            {
                return 0;
            }
            x/=10;
        }
        return 1;
    }
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for(int i =left;i<=right;i++)
        {
            if(helper(i))
            {
                ans.push_back(i);
            }
        }
        return ans;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna