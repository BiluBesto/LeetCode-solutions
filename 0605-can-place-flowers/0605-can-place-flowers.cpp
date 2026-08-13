class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int k=0;
        if(flowerbed.size()==1 && flowerbed[0]==0)
        {
            return true;
        }
        if(flowerbed.size()>=2 && flowerbed[0]==flowerbed[1])
        {
            k++;
            flowerbed[0]= (flowerbed[0]==0)?1:0;
        }
        int prev = flowerbed[0];
        for(int i =1;i<flowerbed.size();i++)
        {
            if(prev!=flowerbed[i])
            {
                prev = flowerbed[i];
            }
            else if(i+1<flowerbed.size() && flowerbed[i+1]!=flowerbed[i])
            {
                prev=flowerbed[i];
            }
            else
            {
                flowerbed[i] = (prev==0)?1:0;
                prev = flowerbed[i];
                k++;
            }
        }

        return (k>=n)? true: false;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna