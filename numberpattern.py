# num=5
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()    

# num=5
# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(col,end=" ")
#     print()    

# num=5
# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(10-col,end=" ")
#     print()    

# 
# num=5
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()    

# num=5
# for row in range(1,num+1):
#     cols=1
#     for col in range(1,row+1):
#         print(format(cols,"2d"),end=" ")
#         cols+=1
#     print()    

# num=15
# for row in range(1,num+1):
#     cols=1
#     for col in range(1,row+1):
#         print(format(cols,"1d"),end=" ")
#         cols+=1
#     print()    

# num=5
# charecter=64
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(chr(charecter+col),end=" ")
#     print()

# num=5
# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

num=5
cols=1
for row in range(1,num+1):
    
    for col in range(1,row+1):
 
        print(row,end=" ")
        col+=1
        
    print()
