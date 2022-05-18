import numpy as np

a = np.array([])
n=int(input("Enter the number of element: "))
for i in range(n):
    element=int(input("Enter Element: "))
    a=np.append(a,element)
print(a)

b =np.flipud(a)
print(type(b[0]))
print(type(a[0]))