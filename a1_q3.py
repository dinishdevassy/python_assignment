import math;

n=int(input("Enter a number : "));
n1=int("%s" %n);
n2=int("%s%s" %(n,n));
n3=int("%s%s%s" %(n,n,n));
res=n1+n2+n3;
print("%d+%d+%d = %d" %(n1,n2,n3,res));