n=int(input())
count=0
n1=n
z=n
ans=0
while n > 0:               
    count=count+1
    n=n//10
while n1 > 0:
    digit=n1%10
    power=digit**count
    ans=ans+power
    n1=n1//10
if ans == z:
    print("yes")
else :
    print("no")
    #disarium