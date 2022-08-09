# list1=["apple","banana","cherry"]
# list2=[1,2,3,4,5]
# print(type(list1))
# print(type(list2))

# list1=[1,2,"peter",4.50,"ricky",5,6]
# list2=[1,2,"peter",4.50,"ricky",5,6]
# print(list1==list2)

# list=[1,2,3,4,5,6,7]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[0:6])
# print(list[:])
# print(list[2:5])
# print(list[1:6:5])

# list=[1,2,3,4,5]
# print(list[-1])
# print(list[-3:])
# print(list[:-1])
# print(list[-3:-1])

#list repetation
# l1=[1,2,3,4,5,6]
# print(l1*3)

#list concatenation
# l1=[1,2,3]
# l2=["a","b","c"]
# print(l1+l2)

#membership in string
# l1=[1,2,3,"a"]
# print("a" in l1)

#string iteration
# l1=[1,2,3,4,5,6]
# for i in l1:
#     print(i)

#string length
#l1=[1,2,3,4,5,6]
#print(len(l1))

#itertion using while
# list1=[1,"hello",4.5]
# index=0
# while index<len(list1):
#     print(list1[index])
#     index+=1

#list append method
# list1=["appple","banana","cherry"]
# list1.append("orange")
# print(list1)

#list insert method
# list1=["appple","banana","cherry"]
# list1.insert(2,"orange")
# print(list1)

#list extend method
# list1=["appple","banana","cherry"]
# list2=["orange","pineapple","papaya"]
# list1.extend(list2)
# print(list1)

#remove data in list

# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

#pop data
# thislist=["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)

#delete entire list

# thislist=["apple","banana","cherry"]
# del thislist
# print(thislist)

#pop()

# thislist=["apple","banana","cherry"]
# thislist.pop()
# print(thislist)

#sort()method is used to sort list permenently

# thislist=["orange","apple","cherry"]
# thislist.sort()
# print(thislist)

#sorted() method is used to sort list temporary or at a tym

# thislist=["orange","apple","cherry"]
# print(thislist)
# print(sorted(thislist))
# print(thislist)

#len(list) method is used to find length of list when it has numeric value

# l1=[1,2,3,4,5,6]
# print(len(l1))

#max(list) is used ti find maximum element of the list
# l1=[34,67,55,8]
# print(max(l1))

#min() is used to return minimum element
# l1=[34,67,55,8]
# print(min(l1))

#list(seq)method is used to covert sequence to list

# tup=(23,6,9,7)
# print(list(tup))

# str="vaishnavi"
# print(list(str))

#  function in list

# def myfunc(n):
#     return abs(n-50)

# thislist=[100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)     

#case insensitive sort

# thislist=["banana","Orange","Kiwi","cherry"]
# thislist.sort()
# print(thislist)

# thislist=["banana","Orange","Kiwi","cherry"]
# thislist.sort(key=str.lower)
# print(thislist)

#reverse order
# thislist=["banana","Orange","Kiwi","cherry"]
# thislist.reverse()
# print(thislist)

# copy a list using copy() method and list()
# thislist=["banana","Orange","Kiwi","cherry"]
# mylist=thislist.copy()
# print(mylist)

# thislist=["banana","Orange","Kiwi","cherry"]
# mylist=list(thislist)
# print(mylist)

#join two list

# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

#join list using append inside for loop

# list1=["a","b","c"]
# list2=[1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1) 
# list1.extend(list2)
# print(list1)   

# list index() method

# fruits=["apple",'banana','cherry']
# x=fruits.index("cherry")
# print(x)

