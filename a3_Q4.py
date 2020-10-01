a=input("Enter a list of numbers : ")
list1=[]
list=list(a.split(" "))
for i in list:
    list1.append(int(i))
list1.sort()
print(list1)
print("second largest : ",list1[-2])
