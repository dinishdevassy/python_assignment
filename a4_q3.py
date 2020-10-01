s=input("Enter the list of numbers : ")
list1=list(s.split(" "))
print(list1)
res=0
i=0
for i in list1:
    res=res+int(i)
print(res)