
#include <vector>

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> levels;  
        if (root != nullptr)
        {
            travers_tree(root, &levels);
        }
        
        return levels;
    }

    void travers_tree(TreeNode* node, std::vector<std::vector<int>>* levels, int level = 0)
    {
        if (levels->size() == level)
        {
            levels->push_back(std::vector<int>());
        }

        levels->at(level).push_back(node->val);

        if (node->left != nullptr)
        {
            travers_tree(node->left, levels, level + 1);
        }

        if (node->right != nullptr)
        {
            travers_tree(node->right, levels, level + 1);
        }

    }
};
