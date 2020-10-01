import math

for i in range(1000,10000):
    val=True
    n=int(i)
    while(n>0):
        a=int(n%10)
        n=n/10
        if a%2!=0:
            val=False
            break
    if(val):
        root=math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            print(i)

