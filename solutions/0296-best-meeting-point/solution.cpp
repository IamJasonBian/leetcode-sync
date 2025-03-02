using namespace std;

class Solution {
public:
    int minTotalDistance(vector<vector<int>>& grid) {
        
        vector<int> xCoords;
        vector<int> yCoords;
        
        for (int row = 0; row < grid.size(); ++row) {
            for (int col = 0; col < grid[0].size(); ++col) {
                if (grid[row][col] == 1) {
                    xCoords.push_back(row);
                }
            }
        }
        
        for (int col = 0; col < grid[0].size(); ++col) {
            for (int row = 0; row < grid.size(); ++row) {
                if (grid[row][col] == 1) {
                    yCoords.push_back(col);
                }
            }
        }
        
        sort(xCoords.begin(), xCoords.end());
        sort(yCoords.begin(), yCoords.end());
        
        
        int medianX = xCoords[xCoords.size() / 2];
        int medianY = yCoords[yCoords.size() / 2];
        
        int totalDistance = 0;
        
        for (int x : xCoords) {
            totalDistance += abs(x - medianX);
        }
        
        for (int y : yCoords) {
            totalDistance += abs(y - medianY);
        }
        
        return totalDistance;
    }
};

