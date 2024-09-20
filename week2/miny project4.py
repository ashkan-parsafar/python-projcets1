def none():
    for i in lst1:
        for y in lst2:
            if i==y:
                d=True
                break
            else:
                d=False
    return d
list1 = input("Enter list 1 ")
list2 = input("Enter list 2 ")
lst1=list1.split(",")
lst2=list2.split(",")
print(none())
