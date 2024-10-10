def LowerOrUpper(name):
    upper,lower,list,result_dict,listNumber = 0,0,[],{},0
    d=name.upper()
    list.extend(d)
    for i in name:
        if i==list[listNumber]:
            upper+=1
        else:
            lower+=1
        listNumber+=1
    result_dict["upper"] = upper
    result_dict["lower"] = lower
    return result_dict

name = input("enter your name: ")
print(LowerOrUpper(name))
