s = "a dictionary python is datastructure and it is in method dictionary of python language"
h=s.split()
d={}
for i in h:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
