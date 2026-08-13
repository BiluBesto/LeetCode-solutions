/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    void minVal(TreeNode *root,int &firstMin)
    {
        if(root)
        {
            firstMin = min(firstMin,root->val);
            if(root->left)
            {
                minVal(root->left,firstMin);
            }
            if(root->right)
            {
                minVal(root->right,firstMin);
            }
        }
    }
    void minVal2(TreeNode *root,long &secondNum,int &firstNum)
    {
        if(root)
        {
            if(root->val>firstNum)
            {
                if(secondNum>root->val)
                {
                    secondNum = root->val;
                }
            }
            if(root->left)
            {
                minVal2(root->left,secondNum,firstNum);
            }
            if(root->right)
            {
                minVal2(root->right,secondNum,firstNum);
            }
        }
    }
    int findSecondMinimumValue(TreeNode* root) {
        int firstMin = INT_MAX;
        long secondMin = LLONG_MAX;
        minVal(root,firstMin);
        cout<<firstMin;
        minVal2(root,secondMin,firstMin);
        return (secondMin!=LLONG_MAX)? (int)secondMin : -1;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna