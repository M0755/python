def  dec2bin(n,d=2):
    ans=""
    while n !=0:
        r = n % d
        ans = str(r)+ans
        #print(r,end=")
        n = n // d
    print(ans)
num=int(input("Enter any number:"))
dec2bin(num)


    
