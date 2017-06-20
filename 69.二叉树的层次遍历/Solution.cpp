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
    /**
     * @param root : The root of binary tree.
     * @return : buttom-up level order a list of lists of integer
     */
public:
    vector<vector<int>> levelOrderBottom(TreeNode *root) {
        // write your code here
        vector<vector<int>> rlt;
        if(root == NULL) return rlt;
        queue<TreeNode *> q;
        q.push(root);
        while(q.size() != 0){
            int size = q.size();
            vector<int> layer;
            for(int i=0; i<size; i++){
                TreeNode* t = q.front();
                q.pop();
                if(t->left != NULL) q.push(t->left);
                if(t->right != NULL) q.push(t->right);
                layer.push_back(t->val);
            }
            if(layer.size() != 0) rlt.push_back(layer);
        }
        reverse(rlt.begin(), rlt.end());
        return rlt;
    }
};