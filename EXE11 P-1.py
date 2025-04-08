def try1():
    a=int(input("Enter First value"))
    b=int(input("Enter Second value"))
    try:
     c=a/b

     print(c)
    except ZeroDivisionError as zde:
        print("Denominator 0???")
        print(zde.args)
        x=input("Press a key")
        print(zde)

    print("I am addicted to my phone")


try1()
    
