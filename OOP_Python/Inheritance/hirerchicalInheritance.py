class circle:
    def __init__(self,r):
        self._r=r
        
    def area(self,r):
        return 3.14*r**2
    
class sphere(circle):
    def __init__(self,r):
        super().__init__(r)
    
    def volume(self):
        return (4/3)*3.14*self._r**3
    
    def display(self):
        print("Sphere :")
        print("Volume :",self.volume())
        
class cylinder(circle):
    def __init__(self,r,h):
        super().__init__(r)
        self.__h = h
        
    def volume(self):
        return 3.14*(self._r**2)*self.__h
    
    def display(self):
        print("Cylinder: ")
        print("Volume: ",self.volume())
        
while(True):
    print("----------MENU------------")
    print("1.Sphere")
    print("2.Cylinder")
    print("3.Close")
    
    ch = int(input("Enter your choice :"))
    if ch == 1:
        r = float(input())
        s = sphere(r)
        s.display()
    elif ch == 2:
        r = float(input())
        h = float(input())
        c = cylinder(r, h)
        c.display()
    elif ch == 3:
        print("Closing program...")
        break
    else:
        print("Invalid choice! Try again.")
    