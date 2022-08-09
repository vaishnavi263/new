# num=float(input("Enter a number:"))
# if num>=0:
#     if num==0:
#         print("Zero")
#     else:
#         print("Positive Number")
# else:
#     print("Negative Number")            
num1=int(input("Eneter first number"))
num2=int(input("Eneter second number"))
num3=int(input("Eneter Third number"))
if num1>num2:
    if num1>num3:
        print("num1 is greatest number")
elif num2>num1:
    if num2>num3:
        print("num2 is greatest number")
    else:
         print("num3 is largest number")  

else:
    print("equal numbers")                  
