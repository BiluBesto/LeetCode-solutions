class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> A,B;
        if (nums1.size()>nums2.size())
        {
            A = nums2;
            B = nums1;
        }
        else
        {
            A = nums1;
            B = nums2;
        }
        int l=0;
        int r=A.size();
        int total=A.size()+B.size();
        int half=total/2;
        while(true)
        {
            int i = (l+r)/2;
            int j = half - i;
            int Aleft=i>0?A[i-1]:INT_MIN;
            int Aright=i<A.size()?A[i]:INT_MAX;
            int Bleft=j>0?B[j-1]:INT_MIN;
            int Bright=j<B.size()?B[j]:INT_MAX;
            if (Aleft <= Bright && Bleft<=Aright)
            {
                if(total%2)
                {
                    return min(Bright,Aright);
                }
                return (max(Aleft,Bleft)+min(Aright,Bright))/(double)2;
            }
            else if(Aleft>Bright)
            {
                r=i-1;
            }
            else
            {
                l=i+1;
            }
        }
    }
};