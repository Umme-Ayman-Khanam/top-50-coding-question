n=int(input())
k=int(input())
a=list(map(int,input().split()))
m=1
z=0
mx=-999
for i in range(1,n):
    b=a[i-1:i+1]
for j in b:
    z+=(j*m)
    m=m+1
if z>mx:
    mx=z
print(z)
