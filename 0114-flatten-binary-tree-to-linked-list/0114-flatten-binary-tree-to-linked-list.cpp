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
    TreeNode *dummy = new TreeNode(0);
    TreeNode *temp = dummy;
    void preOrder(TreeNode *root)
    {
        if(root == nullptr)
        {
            return;
        }
        cout<<root->val<<endl;
        temp->right = new TreeNode(root->val);
        temp->left = nullptr;
        temp = temp->right;
        preOrder(root->left);
        preOrder(root->right);
    }
    void flatten(TreeNode* root) {
        if(!root)
            return;
        preOrder(root);
        root->val = dummy->right->val;
            root->right = dummy->right->right;
        root->left = dummy->right->left;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna