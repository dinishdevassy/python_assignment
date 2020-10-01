s=input("Enter a String : ")
list1=list(s)
count=0
for i in list1:
    if i=='a' or i=='e' or i=='i'or i=='u' or i=='o' :
        count+=1
    elif i=='A' or i=='E' or i=='I'or i=='U' or i=='O' :
        count+=1
print(count)
