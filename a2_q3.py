str1=input("Enter a String : ")
n=len(str1)
#output=str1[n-1]+str1[1:n-1]+str1[0]
output=str1[-1:]+str1[1:-1]+str1[0]
print(output)