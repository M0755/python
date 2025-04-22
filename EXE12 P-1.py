class complexnumbers:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    def add(self,other):
        return complexnumbers(self.real+other.real,self.imaginary+other.imaginary)
    def sub(self,other):
        return complexnumbers(self.real-other.real,self.imaginary-other.imaginary)
    def multiply(self,other):
        realpart=self.real*other.real - self.imaginary*other.imaginary
        imaginarypart=self.real*other.imaginary+self.imaginary*other.real
        return complexnumbers(realpart,imaginarypart)
    def divide(self,other):
        denominator = other.real**2 + other.imaginary**2
        realpart=(self.real*other.real - self.imaginary*other.imaginary) / denominator
        imaginarypart=(self.real*other.imaginary+self.imaginary*other.real) / denominator
        return complexnumbers(realpart,imaginarypart)

a=complexnumbers(6,17)
b=complexnumbers(13,26)
print(complexnumbers.add(a,b))
print(complexnumbers.sub(a,b))
print(complexnumbers.multiply(a,b))
print(complexnumbers.divide(a,b))
        
        
        
        
