str1=input("Enter a String : ")
str2=input("Enter another String : ")
print (str1)
print (str2)
output=str1[0]+str2[1]+str1[1:len(str1)]+" "+str2[0]+str1[1]+str2[1:len(str2)]
# output=str1.replace(str1[1],str2[1],1) +" "+ str2.replace(str2[1],str1[1],1)
print(output)