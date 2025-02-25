l1=[1,2,3,3,3,3,3]
l2=[]
print(list(set(l1)))
list
for i in l1:
    if i not in l2:
        l2.append(i)
        else:
            continue
    print(l2)


