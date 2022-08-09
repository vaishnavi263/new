#pattern printing
# +++++
# -   -
# -   -
# -   -
# +++++
for row1 in range(1,6):
    print("+",end="")
print()    
for row2 in range(1,4):
    for col in range(1,6):

        if col==1 or col==4:
           print("-",end="")
        else:
           print(" ",end="")  
    print()
for row3 in range(1,6):
    print("+",end="")
    
    
    