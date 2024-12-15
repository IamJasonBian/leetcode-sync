class Solution {

private:

  bool is_valid(int x, int y, int m, int n)
  {
    if(x>=0 && x<m && y>=0 && y<n)return true;
    return false;
  }

public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) 
    {
        queue<pair<int,int>>q;
        int m=grid.size();
        int n=grid[0].size();

        vector<int>xt = {1,-1,0,0,1,-1,-1,1};
        vector<int>yt = {0,0,1,-1,1,-1,1,-1};

        q.push({0,0});
        vector<vector<int>>vis(m,vector<int>(n,0));
        vector<vector<int>>dis(m,vector<int>(n,-1));
     
        vis[0][0]=1;
        if(grid[0][0]==1)return -1;
        dis[0][0]=1;

        while(!q.empty())
        {
            pair<int,int>p=q.front();
            q.pop();

           
            for(int i=0;i<8;i++)
            {
                int x=p.first + xt[i];
                int y=p.second + yt[i];

                if(is_valid(x,y,m,n) && !vis[x][y] && grid[x][y]==0)
                {
                    dis[x][y]=dis[p.first][p.second]+1;
                    vis[x][y]=1;
                    q.push({x,y});
                }

            }




        }

      return dis[m-1][n-1];
        
    }
};
