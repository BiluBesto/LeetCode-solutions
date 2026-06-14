#include <cmath>
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<=0)   
            return false;
        while(n>1)
        {
            if(floor(n/3.0)!=ceil(n/3.0))
            {
                return false;
            }
            n/=3;
        }
        return true;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna