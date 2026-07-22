class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int low = 0;
        int mid;
        int high = nums.size()-1;
        while(low<=high)
        {
            mid = (low+high)/2;
            if(nums[mid]==target)
            {
                return true;
            }
            if(nums[mid]==nums[low]&&nums[mid]==nums[high])
            {
                low++;
                high--;
            }
            else if(nums[low]<=nums[mid])
            {
                if(nums[low]<=target && target<nums[mid])
                {
                    high = mid - 1;
                }
                else
                {
                    low = mid +1;
                }
            }
            else
            {
                if(nums[mid]<target && target<=nums[high])
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid - 1;
                }
            }
        }
        return false;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna