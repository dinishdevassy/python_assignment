a=input("Enter Colour : ")
b=input("Enter Colour : ")
color_1=set(a.split(" "))
color_2=set(b.split(" "))
print(color_1.difference(color_2))

