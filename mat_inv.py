import numpy as np

def Inverse(a): #inverse function
    det=0
    for k in range(3):
        det=det+(a[0,k]*(a[1,(k+1)%3]*a[2,(k+2)%3]-a[1,(k+2)%3]*a[2,(k+1)%3]))
    print("Determinant of the matrix ",det)
    for i in range(3):
        for j in range(3):
            ivs[i,j] = ((a[(j+1)%3,(i+1)%3]*a[(j+2)%3,(i+2)%3])-(a[(j+1)%3,(i+2)%3]*a[(j+2)%3,(i+1)%3]))/det
    print("Inverse of the Matrix: ")
    print(ivs)

def Transpose(a): #transpose function
    for i in range(3):
        for j in range(3):
            trans[i,j]=a[j,i] 
    print("Transpose of the Matrix is: ")  
    print(trans)

#driver 
a=np.zeros((3,3))
ivs=np.zeros((3,3))
trans=np.zeros((3,3))
print("Enter the elements row wise")
for i in range(3):
    for j in range(3):
        b=input()
        a[i,j]=int(b)
print(a)
Inverse(a)
Transpose(a)

      
      
