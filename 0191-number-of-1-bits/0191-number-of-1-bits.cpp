#include <cmath>
class Solution {
public:
    int hammingWeight(int n) {
        int res = 0;
        int a,b;
        while(n>0)
        {
            a  = floor(n/2.0);
            b = ceil(n/2.0);
            n/=2;
            if(a!=b)
            {
                res+=1;
            }
            cout << a << ' '<<b;
        }
        return res;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna