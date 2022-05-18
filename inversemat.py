import numpy as np
a=np.zeros((3,3))
ivs=np.zeros((3,3))
print(a)
print("Enter the elements row wise")
for i in range(3):
    for j in range(3):
        b=input()
        a[i,j]=int(b)
print(a)
det=0
for k in range(3):
    det=det+(a[0,k]*(a[1,(k+1)%3]*a[2,(k+2)%3]-a[1,(k+2)%3]*a[2,(k+1)%3]))
print(det)
for i in range(3):
    for j in range(3):
        ivs[i,j] = ((a[(j+1)%3,(i+1)%3]*a[(j+2)%3,(i+2)%3])-(a[(j+1)%3,(i+2)%3]*a[(j+2)%3,(i+1)%3]))/det
print(ivs)   
        

      
      
