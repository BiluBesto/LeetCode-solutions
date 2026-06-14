class Solution {
public:
    bool numDivides(int num, int n)
    {
        if(num%n==0)
            return true;
        return false;
    }
    bool checkPerfectNumber(int num) {
        if(num==1) return false;
        int r = 1;
        int n = 2;
        int alnum = num;
        while(n<=num/2)
        {
            if(numDivides(num,n))
            {
                r+=n;
            }
            n++;
        }
        cout<<r;
        if(r==num)
            return true;
        return false;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna