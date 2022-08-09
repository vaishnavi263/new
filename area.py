

print("Enter your choice\n1:area of rectangle\n2:area of square\n3:area of cicle\n4:area of triangle")
choice=int(input("enter your choice"))

if(choice==1):
    length=float(input("Enter the length"))
    breadth=float(input("enter the breadth"))
    print(length*breadth)
elif(choice==2):
    length=float(input("Enter the length"))
    print(length*length)
elif(choice==3):
    radius=float(input("Enter the radius"))
    print(3.14*radius*radius)
elif(choice==4):
    length=float(input("Enter the length"))
    breadth=float(input("enter the breadth"))
    print(.5*length*breadth)
else:
    print("invalid choice")    

    






