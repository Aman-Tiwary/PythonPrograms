import numpy as np
def matrix_mul(arr1,arr):
    mat = arr1[::-1]
    len1 = len(arr1)
    len2 = len(arr)
    len3 = len1+len2-1
    
    for i in range(len2-1,len3):
        arr = np. append(arr,0)
    print(arr)
    res = np.zeros((len3,len1))
    for j in range(len1):
        k=0
        for i in range(len3):
            if i>=j:
                res[i][j] = arr[k]
                k+=1
    print(res)
    result = np.array([])
    for i in range(0,len3):
        sum =0
        for j in range(0,len1):
            ele = 0
            ele = res[i][j]*mat[j]
            sum += ele
        result = np.append(result,sum)
    print(result)
a=np.array([1,2,3])
b=np.array([1,2,3])
matrix_mul(a,b)