import numpy as np
mat = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        a = int(input("Enter elements row-wise"))
        mat[i,j]=a
adj = np.zeros((4,4))
invs = np.zeros((4,4))

def getCofactor(mat, temp, p, q, n)
    i = 0
    j = 0
    #Looping for each element of the matrix
    for row in range(n):
        for col in range(n):
            #Copying into temporary matrix only those element
            #which are not in given row and column
            if row != p and  col != q :
                temp[i,j] = A[row,col]
                j=j+1
                #Row is filled, so increase row index and
                #reset col index
                if j == n - 1:
                    j = 0
                    i=i+1
def determinant(mat, n)
    D = 0; #Initialize result
    #Base case : if matrix contains single element
    if n == 1:
        return mat[0,0]
    temp = np.array((4,4)) #To store cofactors
    sign = 1;  #To store sign multiplier
    #Iterate for each element of first row
    for f in range(n):
        #Getting Cofactor of A[0][f]
        getCofactor(mat, temp, 0, f, n);
        D =D+( sign * mat[0,f] * determinant(temp, n - 1))
        #terms are to be added with alternate sign
        sign = -sign
    return D

def adjoint(mat,adj)
    if N == 1:
        adj[0,0] = 1
        return
    #temp is used to store cofactors of A[][]
    sign = 1
    temp=np.zeros((4,4))
    for i in range(N):
        for j in range(N):
            #Get cofactor of A[i][j]
            getCofactor(A, temp, i, j, N)
            #sign of adj[j][i] positive if sum of row
            #and column indexes is even.
            sign=((i+j)%2==0)?1:-1
            #Interchanging rows and columns to get the
            #transpose of the cofactor matrix
            adj[j,i]= (sign)*(determinant(temp, N-1))

def inverse(mat[N,N],invs[N,N])
    #Find determinant of A[][]
    det = determinant(mat, N)
    if det == 0:
        print("Singular matrix, can't find its inverse")
        return False
 
    #Find adjoint
    adj = np.zeros(4,4)
    adjoint(mat, adj)
 
    #Find Inverse using formula "inverse(A) = adj(A)/det(A)"
    for i in range(N):
        for j in range(N):
            inverse[i,j] = adj[i,j]/float(det)
    return True
 
#Generic function to display the matrix.  We use it to display
#both adjoin and inverse. adjoin is integer matrix and inverse
#is a float.
template<class T>
void display(T A[N][N])
{
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
            cout << A[i][j] << " ";
        cout << endl;
    }
}


 
    int adj[N][N];  // To store adjoint of A[][]
 
    float inv[N][N]; // To store inverse of A[][]
 
    cout << "Input matrix is :\n";
    display(A);
 
    cout << "\nThe Adjoint is :\n";
    adjoint(A, adj);
    display(adj);
 
    cout << "\nThe Inverse is :\n";
    if (inverse(A, inv))
        display(inv);
 
    return 0;
}