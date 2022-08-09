


number=int(input("enter the number"))
temp=number
rev=0
while number>0:
    rem=number%10
    rev=rev*10+rem
    number//=10
if temp==rev:
    print("palindrome")
else:    
    print("not palindrome")    