class box:
    def  __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height
    def volume(self):
        return self.length*self.breadth*self.height

class box1(box):
    def __init__(self,height,length,breadth):
       super().__init__(length,breadth,height)
    def volume(self):
        return self.length*self.breadth*self.height
    
     
height=float(input("Enter the height of the box"))
length=float(input("Enter the length of the box "))
breadth=float(input("Enter the breadth of the box"))


vol= box(length,breadth,height)
print(vol.volume())
vol1=box1(length,breadth,height)
print(vol1.volume())
