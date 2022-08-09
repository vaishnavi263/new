# str1=input("Enter the string")
# rev=str1[::-1]
# if str1==rev:
#     print("palindrome")
# else:
#     print("not palindrome")    
# num=-4.5
# if num>0:
#     print("Positive number")
# elif num==0:
#     print("Zero")
# else:    
#     print("Negative number")    
# num=int(input("enter a no."))
# if num==1:
#     print("Sundsy")
# elif num==2:
#     print("Monday")
# elif num==3:
#     print("tuesday")
# elif num==4:
#     print("wednessday")
# elif num==5:
#     print("thursday")
# elif num==6:
#     print("friday")
# elif num==7:
#     print("saturday")
# else:
#     print("invalid choice")      


# num1=int(input("enter your first number"))
# num2=int(input("enter your second number"))
# print("1.Addition \n 2.Substraction \n 3.Multiplication \n 4.division")
# choice=int(input("Enter your choice"))
# if choice==1:
#     print(num1+num2)  
# elif choice==2:
#     print(num1-num2)
# elif choice==3:
#     print(num1*num2)  
# elif choice==4:
#     print(num1/num2)  
# else:
#     print("invalid choice")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter thirs number"))
if (num1>num2) and (num1>num3):
    print("largest number is",num1)
elif (num2>num1) and (num2>num3):
        print("largest number is",num2)
elif (num3>num1) and (num3>num2):
        print("largest number is",num2)
else:
    print("Numbers are equal") 
if (num1<num2) and (num1<num3):
    print("smallest number is",num1)
elif (num2<num1) and (num2<num3):
        print("smallest number is",num2)
elif (num3<num1) and (num3<num2):
        print("smallest number is",num2)


        

