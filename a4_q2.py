n=int(input("Enter Limit : "))
f=0
s=1
print (f)
print(s)
c=0
while(c<n-2):
    t=f+s
    f=s
    s=t
    c=c+1
    print(t)