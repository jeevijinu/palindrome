a=int(input("enter num : "))
temp=a
rev=0
while(a>0):
  rev=(rev*10)+a%10
  a=a//10
if(temp==rev):
 print("palindrome")
else:
    print("not a palindrome")

    
    
