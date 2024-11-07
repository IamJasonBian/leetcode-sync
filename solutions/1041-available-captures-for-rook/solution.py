class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        a=board
        for i in range(0,8):
            for j in range(0,8):
                if a[i][j]=='R':
                    m=i
                    n=j
        count=0

        #up 
        for i in range(1,m+1):
            if a[m-i][n]=='p':

                count+=1
                break
            elif a[m-i][n]=='B':
                break
            else:
                continue

        #down 
        for i in range(1,8-m):
            if a[m+i][n]=='p':
                count+=1

                break
            elif a[m+i][n]=='B':
                break
            else:
                continue


        #left 
        for i in range(1,n+1):
            if a[m][n-i]=='p':
                count+=1
                break


            elif a[m][n-i]=='B':
                break
            else:
                continue
        #right
        for i in range(1,8-n):
            if a[m][n+i]=='p':
                count+=1
                break
            elif a[m][n+i]=='B':
                break
            else:
                continue
        return count
