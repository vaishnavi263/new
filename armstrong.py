

num=(input("Enter the number"))
sum=0
leng=len(num)
temp=num=int(num)
while num>0:
    rem=num%10
    sum=sum+rem**leng
    num=num//10
if sum==temp:
    print("armstrong number")
else:
    print("not armstrong")        
