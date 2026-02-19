class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
         int a = abs(target[0]) + abs(target[1]);

        for (auto& b : ghosts) {
            int c = abs(target[0] - b[0]) + abs(target[1] - b[1]);
            if (c <= a) return false;
        }
        return true;
        
    }
};
