#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#column are set to 0. 
def tozero(mat):
    l=[]
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            if(mat[i][j]==0):
                   l=l+[(i,j)]
    for i in range(0,len(l)):
        for j in range(0,len(mat)):
             mat[l[i][0]][j]=0  
        for j in range(0,len(mat[0])):
             mat[j][l[i][1]]=0   
    print(mat)
    
    
tozero([[1,0,0],[1,0,1],[1,1,1]])
