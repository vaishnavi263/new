# for row1 in range(1,10):
#     print("*",end="")
# print()
# for row2 in range(1,10):
#     for col in range(1,10):
        
#         if row2==4:
#             print("* hello *",end="")
#             break 
#         if col==1 or col==9:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print() 
# for row3 in range(1,10):
#     print("*",end="") 
# print()                  


for row1 in range(1,5):
    print("-",end="")
print()
for row2 in range(1,4):
    for col in range(1,5):
        if col==1 or col==4:
            print("|",end="")
        else:
            print(" ",end="")
    print() 
for row3 in range(1,5):
    print("-",end="") 
print()                  
