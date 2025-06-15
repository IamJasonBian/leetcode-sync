class Solution {
    int box_size;
public:
    static bool myCmpLogs(vector<int>&a,vector<int>&b){
        return a[1]<=b[1];
    }
    static bool myCmpQueries(vector<int>&a,vector<int>&b){
        if(a[3]==b[3]){
            return a[1]<=b[1];
        }

        return a[3]<=b[3];
    }

    void add(unordered_map<int,int>&freqMap,vector<int>&log){
        freqMap[log[0]]++;
        return ;
    }
    void remove(unordered_map<int,int>&freqMap,vector<int>&log){
        freqMap[log[0]]--;

        if(freqMap[log[0]]==0){
            freqMap.erase(log[0]);
        }
        return ;
    }
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& Queries) {
        int boxSize = sqrt(logs.size());
        this->box_size = boxSize;
        logs.push_back({INT_MIN,INT_MIN});
        logs.push_back({INT_MAX,INT_MAX});
        sort(logs.begin(),logs.end(),myCmpLogs);
        vector<vector<int>> queries;
        for(int i = 0;i<Queries.size();i++){
            queries.push_back({Queries[i]-x,Queries[i],i,(Queries[i]-x)/boxSize});
        }
        sort(queries.begin(),queries.end(),myCmpQueries);

        unordered_map<int,int> freqMap;
        vector<int> ans(queries.size(),0);

        int L = 0;
        int R = 0;

        for(int i =0;i<queries.size();i++){
            while(R>0 and R<logs.size() and logs[R][1]>queries[i][1]){
                R--;
                remove(freqMap,logs[R]);
            }

            while(R>=0 and R<logs.size() and logs[R][1]<=queries[i][1]){
                add(freqMap,logs[R]);
                R++;
            }

            while(L>0 and L<logs.size() and logs[L][1]>=queries[i][0]){
                L--;
                add(freqMap,logs[L]);
            }

            while(L>=0 and L<logs.size() and logs[L][1]<queries[i][0]){
                remove(freqMap,logs[L]);
                L++;
            }

            ans[queries[i][2]]=(n-freqMap.size());
            if(freqMap.find(INT_MIN)!=freqMap.end()){
                ans[queries[i][2]]++;
            }
            if(freqMap.find(INT_MAX)!=freqMap.end()){
                ans[queries[i][2]]++;
            }
        }

        return ans;
    }
};
