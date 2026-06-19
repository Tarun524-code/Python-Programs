class Student :
    def __init__(self, rno, name, branch, section):
        self._rno = rno
        self._name = name 
        self._branch = branch 
        self._section = section 
    
    def printDetails(self):
        print("Student Details :")
        print("------------------------")
        print("Roll no :",self._rno)
        print("Name :",self._name)
        print("Branch :",self._branch)
        print("Section :", self._section)
        
class Marks(Student):
    def __init__(self,rno, name, branch, section, m1, m2, m3):
        super().__init__(rno, name, branch, section)
        self._m1 = m1 
        self._m2 = m2 
        self._m3 = m3 
        
    def printMarks(self):
        print("Marks of subject :")
        print("----------------------")
        print("Subject 1 :", self._m1)
        print("Subject 2 :", self._m2)
        print("Subject 3 :", self._m3)
        
class MarksReport(Marks):
    def __init__(self, rno, name, branch, section, m1, m2, m3):
        super().__init__(rno, name, branch, section, m1, m2, m3)
        
    def total(self):
        tot = self._m1 + self._m2 + self._m3 
        return tot 
    
    def avg(self):
        return self.total()/3
    
    def grade(self):
        tot = self.total() 
        if tot > 290:
            return 'A'
        elif tot > 250:
            return 'B'
        else:
            return 'C'

rno = int(input("Enter roll no: "))
name = input("Enter name :")        
branch = input("Enter branch :")
section = input("Enter section :")
m1 , m2, m3 = map(int, input("Enter marks for 3 subjects :").split())
a = MarksReport(rno, name, branch, section, m1, m2, m3)

a.printDetails()
a.printMarks()
print("----------------------------")
print("Total marks :",a.total(),"\nAverage marks :",a.avg(),"\nGrade :",a.grade())