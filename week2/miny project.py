def multip(lstNumbers):
    result = 1
    for i in lstNumbers:
        result *= int(i)
    return result
numbers = input("Enter your numbers with comma(,)")
lst = numbers.split(",")
print(multip(lst))
