class Solution {
public:
    string toHex(int num) {
        if(!num) return "0";
        unsigned int Num = num;
        string res;
        string hex = "0123456789abcdef";

        while(Num)
        {
            res+=hex[Num%16];
            Num/=16;
        }
        reverse(res.begin(),res.end());
        return res;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna