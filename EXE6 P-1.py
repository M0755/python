l1=[('Darshit','Ashit','Devang'),'Ragi', 'Aashna','Darshini',('Darshil')]
bcount=0
gcount=0
for name in l1:
    if (isinstance(name,tuple)):
        for a in name:
             bcount+=1
    else:
        gcount+=1

print("Number of boys",bcount)
print("Number of girls",gcount)
