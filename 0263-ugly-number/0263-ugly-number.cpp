class Solution {
public:
    bool isMult3(int n)
    {
        int res = 0;
        while(n>0)
        {
            res+=(n%10);
            n/=10;
        }
        if(res%3==0 && res!=0)
        {
            return true;
        }
        return false;
    }
    bool isUgly(int n) {
        while((n%5)==5 || (n%5) == 0 && n!=0)
        {
            n/=5;
        }
        while(isMult3(n))
        {
            n/=3;
        }
        while((n%2)==0 && n!=0)
        {
            n/=2;
        }
        cout<<n;
        if(n==1)
        {
            return true;
        }
        return false;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna