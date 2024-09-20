def MaxNumber(number):
    number=0
    for i in lst:
        d=int(i)
        if d>number:
            number=d
    return number
numbers = input("Enter your numbers with comma(,)")
lst = numbers.split(",")
print(MaxNumber(lst))
