def Sum(lstNumbers):
    result = 0
    for i in lstNumbers:
        result += int(i)
    return result
numbers = input("Enter your numbers with comma(,)")
lst = numbers.split(",")
print(Sum(lst))
