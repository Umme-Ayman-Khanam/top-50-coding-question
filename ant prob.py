steps=int(input())
b=list(map(int, input().split()))
a=0
ans=0
for i in b:
    a=a+i
    if a==0: 
        ans=ans+1
print (ans)