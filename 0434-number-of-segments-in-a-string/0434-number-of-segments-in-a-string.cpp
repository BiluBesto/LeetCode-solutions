class Solution {
public:
    int countSegments(string s) {
        int res = 0;
        bool flag = false;
        bool sflag = false;
        if(s.size()>0&&s[0]!=' ')
        {    res = 1;
             flag = true;
             sflag = true;
        }
        for(char c:s)
        {
            if(c == ' ' && flag)
            {
                res++;
                flag = false;
            }
            else if(c!=' ')
            {
                
                flag = true;
            }
        }
        if(flag && !sflag) res++;
        if(!flag && res!=0 && sflag)
            res--;
        return res;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna