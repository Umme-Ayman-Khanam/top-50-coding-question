n=int(input())
a=list(map(int,input().split()))
a.sort()
j=n-1
b=[]
ans=0
for i in range(0,len(a)):
    if i<j:
        c=abs(a[i]-a[j])
        b.append(c)
        j-=1
for i in b:
    ans=ans+i
print(ans)






























































































































