def w():
 L=float(input("Enter the length of rectangle:"))
 B=float(input("Enter the breadh of rectangle:"))
 Area=L*B
 Perimeter=2*(L+B)
 if Area>Perimeter:
     print("Area is greater than Perimeter")
 elif Area==Perimeter:
     print("Both are Equal")
 else:
     print("Area is smaller than Perimeter")

w()
    
