class rectangle:
    def __init__(self,length,breadth):
        self._length = length
        self._breadth = breadth
    
    def area(self):
        return self._length*self._breadth
    
    def perimeter(self):
        return 2*(self._length+self._breadth)

class cuboid(rectangle):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.__height = height
    
    def volume(self):
        return self._length*self._breadth*self.__height

    def display(self):
        print("Area: ",self.area())
        print("Perimeter: ",self.perimeter())
        print("Volume: ",self.volume())
    
l,b,h = map(int,input().split())
c=cuboid(l,b,h)
c.display()