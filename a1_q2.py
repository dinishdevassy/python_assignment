import math;

str=input("Enter 3 values seperated by ',' :- ");
a=str.split(",");
print("Largest = "+max(a[0],a[2],a[1]));