class Solution {
public:
    bool check(char b,char a){
        if(b - a == 1){
            return true;
        }
        else if(b == 'a' && a == 'z'){
            return true;
        }
        return false;
    }
    int findSubstringInWraproundString(string s) {
        int n = s.length();
        vector<int> v(n,1);
        for(int i = 1;i<s.length();i++){
            if(check(s[i],s[i-1])){
                v[i] = v[i-1]+1;
            }
        }
        vector<int> ans(26,0);
        for(int i = 0;i<s.length();i++){
            ans[s[i]-'a'] = max(ans[s[i]-'a'],v[i]);
        }
        int sum = 0;
        for(auto it:ans){
            sum+=it;
        }
        return sum;
    }
};
