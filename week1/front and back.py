import random
d = {
    "front":0,
    "back":0
}
front = 0
back = 0
chanseNumber=int(input("enter number"))
for u in range(chanseNumber):
    for i in range(17):
        d[random.choice(list(d.keys()))] += 1
    if d["back"]>d["front"]:
        back+=1
    else:
        front+=1
    print(d)
    d["back"]=0
    d["front"]=0
print("front :",front,"back :",back)
