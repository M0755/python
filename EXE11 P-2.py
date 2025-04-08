def try2():
    try:
        a=int(input("Enter an integer value"))
    except ValueError as Ve:
        print(Ve.args)
        try2()

try2()
