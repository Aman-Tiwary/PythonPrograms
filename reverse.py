a=[]
n=int(input("Enter the number of element: "))
for i in range(n):
    element=int(input("Enter Element: "))
    a.append(element)
print(a)

start = 0
end = len(a)-1

while(start<end):
    temp = a[start]
    a[start] = a[end]
    a[end] = temp
    start+=1
    end-=1
print(a)

