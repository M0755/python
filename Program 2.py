def ls():
 a=float(input("Enter the value of a="))
 b=float(input("Enter the value of b="))
 c=float(input("Enter the value of c="))
 largest=a
 if b>largest:
    print(" largest=b")
 if c>largest:
    print(" largest=c")
 smallest=a
 if b<smallest:
    print(" smallest=b")
 if c<smallest:
    print(" smallest=c")
 if largest==smallest:
    print(" all are equal")
 else:
    print(largest,smallest)

ls()
