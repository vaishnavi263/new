# check triangle is scalane,isosulus,equilatoral
# side1=int(input("enter one side"))
# side2=int(input("enter one side"))
# side3=int(input("enter one side"))
# if side1==side2==side3:
#     print("triangle is equilatoral" )
# elif side1==side2 or side1==side3 or side2==side3:
#     print("triangle is isosulus")   
# else:
#     print("triangle is scalane")    


# string="hello world"
# print(string*3)



# limit=int(input("enter the number"))

# fact=1
# sum=0
# for i in range(1,limit+1):
#     fact=fact*i
#     sum=sum+fact
# print(sum)    
    
# num=int(input("enter the number"))
# iter=2

# while iter<num:
#     if num%iter==0:
#         print("prime")
#         break
#     else:
#         print("not")
#         iter=iter+1

#concatenate 2 string
# string1="hello"
# string2="world"
# print(string1+string2)

#check vowel or not
# character=input("enter the charecter")
# vowel=['a','e','i','o','u']
# if (character in vowel):
#     print("vowel")
# else:
#     print("not")    

#fobonacci series
# limit=int(input("enter the limit"))
# num1=0
# sum=0
# num2=1
# while limit>sum:
#     print(sum,end=" ")
#     num1=num2
#     num2=sum
#     sum=num1+num2

#pattern

# num=5

# for row in range(5,0,-1):
#     for col in range(row+1):

    

#         print(col,end=" ")
    
        
#     print()    


# number=int(input("enter the number"))
# for i in range(1,number+1):
#     if number%i==0:
#         print(i,end=" ")

#convert integer to string
# num=12345
# print(str(num))
#check 3 digit number or not
# number=int(input("enter the number"))
# length=len(str(number))
# if length==3:
#     print("3 digit number")
# else:
#     print("not a 3 digit number")    

#1++49
#2++48
#.....
#49++1

# number=50
# start=1
# stop=49
# while start<number:
#     print(start,"++",stop)
#     start+=1
#     stop-=1

#reverse 3 integer number
# number=234
# length=len(str(number))
# for i in range(length-1,-1,-1):
#     print(str(i))

#string slicing
# string="hello world"
# print(string[1:5:2])

#check last number is divisible by 3
# number=int(input("enter the number"))
# digit=number%10
# if digit%3==0:
#     print("divisible")
# else:
#     print("not divisible")    

#print all charecters using for loop
# string="hello world"
# for i in string:
#     print(i)

#print whole numbers using while loop
# number=0
# while number<=10:
#     print(number)
#     number+=1

#pattern


# for row in range(1,6):
#     for col in range(1,6):
#         if col<=row:
#             print(row,end=" ")
#         else:
#             print(col,end=" ")    
#     print()    

#check string is uppercase
# string="VAISHNAVI"
# print(string .isupper())

#display last digit
# num=int(input("enter the number"))
# digit=num%10
# print(digit)

#first 10 natural numbers

# num=1
# while num<=10:
#     print(num)
#     num+=1

#series 1,4,9,16.....
# num=int(input("enetr the limit"))
# for i in range(1,num+1):
#     print(i**2,end=" ")

#print odd no.s
# num=1
# while num<=20:
#     if num%2!=0:
#         print(num,end=" ")
#     num+=1

#uppercase first and last charecter of string
# string="vaishnavi"
# print(string[0].upper()+string[1:-1]+string[-1].upper())

#print "hello if a number is enterd by user is a multiple of 5"

# number=int(input("enter a number"))
# if number%5==0:
#     print("Hello")
# else:
#     print("Bye")    

#print all numbers from 0 to 6 except 3&6
# num=1
# for i in range(1,7):
#     if i==3 or i==6:
#         continue
#     print(i)

#pattern

# num=5
# space=5
# for row in range(1,num+1):
#     for sp in range(space):
#         print(" ",end=" ")
#     space-=1    
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()    
#8
#uppercase or lowercase entire string

# string="luminar TechnoLab"
# print(string.upper())
# print(string.lower())

#check a number is divicible by 7

# number=int(input("enetr e number"))
# if number%7==0:
#     print("number is divisible by 7")
# else:
#     print("not divisible")    

#first 10 even no.s using while loop

# num=0
# while num<20:
#     print(num)
#     num+=2

#check alphabet is vowel or consent using for loop

# char=input("enter the charecter: ")
# for i in char:
#     if i=="a" or i=="e" or i=="i" or i=="o"or i=="u":
#         print("vowel")
#     else:
#         print("consanant")    

#pattern

# num1=5
# num2=5
# space=5
# for row in range(num1,0,-1):
#     for sp in range(space):
#         print(" ",end="")
#     space+=1    
#     for col in range(row):
#         print("*",end=" ")    
#     print()    
# for row in range(1,num2+1):
#     for sp in range(space):
#         print(" ",end="")
#     space+=1    
#     for col in range(row):
#         print("*",end=" ")    
#     print()    

#9
# integer added to a string
# string="luminar"
# num=123
# print(string+str(num))

#check no.is even or not
# number=int(input("enter e number: "))
# if number%2==0:
#     print("even number")
# else:
#     print("odd number")    

#print first 10 numbers and their squares using while loop
# num=1
# while num<=10:
#     print(num,num*num)
#     num+=1

#mutiplication table of 24 using for loop

# num=24
# for i in range(1,11):
#     print(i,"*",num,"=",i*num)

#question paper 1

#string multiplying a string by 3

# string="luminar"
# print(string*3)

#accept 3 sides of triangle and check equilateral,isoscles or scalane

# side1=int(input("enter the 1st side"))
# side2=int(input("enter the 2nd side"))
# side3=int(input("enter the 3rd side"))
# if side1==side2==side3:
#     print("Equilateral triangle")
# elif side1==side2 or side1==side3 or side3==side2:
#     print("isoscles triangle")    
# else:
#     print("scalane triangle")

# prime or not

# num=int(input("enter the number"))
# iter=2

# while iter<num:
#     if num%iter==0:
#         print("prime")
#         break
#     else:
#         print("not")
#         iter=iter+1

#1+2+6+24+120+.....nterms

# num=int(input("enter the limit"))
# fact=1
# sum=0
# for i in range(1,num):
#     fact=fact*i
#     sum=sum+fact
# print(sum)

# num=5
# no=1
# for row in range(num,0,-1):
#     for col in range(1,row+1):
#         print(no,end=" ")
#     no+=1
#     print()    
