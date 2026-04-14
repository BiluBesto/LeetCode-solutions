class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size()-1;
        digits[i]+=1;
        x:
        if(i>0&&digits[i]==10)
        {
            digits[i]=0;
            digits[--i]+=1;
            goto x;
        }
        if(i==0&&digits[i]==10)
        {
            digits[0]=0;
            digits.insert(digits.begin(),1);
        }
        return digits;
    }
};