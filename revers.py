# string=input("enter your string")
# for i in string:
#     print(string[::-1])
# number=(input("enter the number"))
# count=0
# length=len(number)
# print("total number of digits is",length)
# for char in range(len(string)-1,-1,-1):
    # print(string[char])




# num,rev=123,0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num//=10
# print(rev)    

# num=3456
# print(str(num)[::-1])


rev=""
num=123
for i in range(len(str(num))-1,-1,-1):
    rev+=str(num)[i]
print(int(rev))    
