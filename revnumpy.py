import numpy as np

def reverse_arr(a):
    start = 0
    end = len(a)-1

    while(start<end):
        temp = a[start]
        a[start] = a[end]
        a[end] = temp
        start+=1
        end-=1
    return a
arr = np.array([1,2,3])
nr = arr
print(arr)
n_arr=reverse_arr(nr)
print(arr)
print(n_arr)




