a=int(input("Enter a year:"))
if(a%4==0 or a%100==0 or a%400==0):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")
    
