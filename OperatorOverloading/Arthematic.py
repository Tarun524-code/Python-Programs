class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, p1):
        p3=point(0,0)
        p3.x=self.x+p1.x
        p3.y=self.y+p1.y
        return p3
    def __sub__(self, p1):
        p3=point(0,0)
        p3.x=self.x-p1.x
        p3.y=self.y-p1.y
        return p3
    def __mul__(self, p1):
        p3=point(0,0)
        p3.x=self.x*p1.x
        p3.y=self.y*p1.y
        return p3
    def __truediv__(self, p1):
        p3=point(0,0)
        p3.x=self.x/p1.x
        p3.y=self.y/p1.y
        return p3
    def __str__(self):
        return f"({self.x}, {self.y})"

print("Enter the two points of P1")
n1=int(input("Enter the input of n1 in P1"))
n2=int(input("Enter the input of n2 in P1"))
m1=int(input("Enter the input of m1 in P2"))
m2=int(input("Enter the input of m1 in P2"))

p1=point(n1,n2)
p2=point(m1,m2)

print("Record")
print("Point p1",p1)
print("Point p2",p2)
print("SUM of Two points",p1+p2)
print("Sub of Two points",p1-p2)
print("Mul of Two points",p1*p2)
print("Div of Two points",p1/p2)