class Solution {
    bool isOperator(string token) {
        bool res = false;
        if (token == "+" || token == "-" ||
            token == "*" || token == "/") {
            res = true;
        }
        return res;
    }
public:
    int evalRPN(vector<string> &tokens) {
        
    }
};
