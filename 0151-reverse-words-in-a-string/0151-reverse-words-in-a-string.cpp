class Solution {
public:
    string trim(string s)
    {
        string whitespace=" ";
        int start = s.find_first_not_of(whitespace);
        int end = s.find_last_not_of(whitespace);
        return s.substr(start,end-start+1);
    }
    string reverseWords(string s) {
        s=trim(s);
        string res = "";
        int i = s.size()-1;
        while(i>=0)
        {
            while(i>=0&&s[i]==' ')
                i--;
            if(i<0)
                break;
            int j = i;
            while(j>=0&&s[j]!=' ')
                j--;
            res+=s.substr(j+1,i-j);
            while(j>=0&&s[j]==' ')
                j--;
            if(j>=0)
                res+=' ';
            i=j;

            i=j;
        }
        return res;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna