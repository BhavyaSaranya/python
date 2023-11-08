class Teacher:
    __subjects1:str=""
    __subjects2:str=""
    __subjects3:str=""
    def __init__(self):
        pass
    def  setsubjects(self,subjects1:str,subjects2:str,subjects3:str):
        self.__subjects1=subjects1
        self.__subjects2=subjects2
        self.__subjects3=subjects3
    def getsubjects(self):
            return self.__subjects1, self.__subjects2, self.__subjects3


sub=Teacher()
sub.setsubjects("tel","eng","hin")
print(sub.getsubjects())



class Student(Teacher):
    __stdName:str="bhavya"
    __stdRno:int=25

    def __init__(self, stdname, stdrno):
        super().__init__()
        self.__stdName=stdname
        self.__stdRno=stdrno

    def stdDetails(self):
        return self.__stdName,self.__stdRno

class Studentmarks(Student):
    __telMarks:int=""
    __engMarks:int=""
    __hinMarks:int=""
    def __init__(self,stdname,rno):
        super().__init__(stdname,rno)
        pass
    def __init__(self, telmarks, engmarks, hinmarks):
        self.__telMarks=telmarks
        self.__engMarks=engmarks
        self.__hinMarks=hinmarks

    def stdfullMarks(self):
          return self.__telMarks + self.__engMarks + self.__hinMarks


class Stdattendance(Student):
    __totalworkdays:int=""
    __presentdays:int=""
    def __init__(self,stdname, rno):
        super().__init__(stdname,rno)
        pass
    def __init__(self,totalworkdays,presentdays):
        self.__totalworkdays=totalworkdays
        self.__presentdays=presentdays
    def absentdays(self):
        return self.__totalworkdays - self.__presentdays

std = Studentmarks(35,75,90)
details = std.stdDetails()
print(details)
std.setsubjects("tel", "eng", "hin")
std.getsubjects()
marks=std.stdfullMarks()
print(marks)


