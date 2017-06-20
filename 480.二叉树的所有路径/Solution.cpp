/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param root the root of the binary tree
     * @return all root-to-leaf paths
     */
    vector<string> binaryTreePaths(TreeNode* root) {
        // Write your code here
        vector<string> rlt;
        if(root == NULL) return rlt;
        vector<string> l = binaryTreePaths(root->left);
        for(int i=0; i<l.size(); i++){
            string s = to_string(root->val) + "->" + l[i];
            rlt.push_back(s);
        }
        
        vector<string> r = binaryTreePaths(root->right);
        for(int i=0; i<r.size(); i++){
            string s = to_string(root->val) + "->" + r[i];
            rlt.push_back(s);
        }
        if(rlt.size() == 0) rlt.push_back(to_string(root->val));
        return rlt;
    }
};