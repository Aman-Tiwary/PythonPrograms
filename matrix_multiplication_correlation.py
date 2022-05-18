import numpy as np
def matrix_mul_corr(arr1,arr2):
    rev_arr = arr2[::-1]
    len1 = len(arr1)
    len2 = len(arr2)
    res_arr = np.array([])
    len3 = len1+len2-1

    for k in range(len3):
        sum = 0
        for i in range(len1):
            for j in range(len2):
                if k == i+j:
                    current_el = 0
                    current_el = arr1[i]*rev_arr[j]
                    sum += current_el
        res_arr = np.append(res_arr,sum)
    return res_arr
a = np.array([1,2,3])
print(matrix_mul_corr(a,a))

