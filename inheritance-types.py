#multi-level & hierarchical inheritance
class Address:
    __address: str = ""

    def addAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

class Employee(Address):
    __firstname : str = ""
    __lastname : str = ""
    __surname : str = ""

    def setName(self, fname, lname, sname):
       self.__firstname = fname
       self.__lastname = lname
       self.__surname = sname
    def __nameFormat(self):
        return f'{self.__firstname} {self.__lastname} {self.__surname}'

    def getFullname(self):
        return self.__nameFormat()
class perminentEmployee(Employee):
     __sal : int = 20000
     def salCal(self, months : int):
         return f'salary for {months} is  {self.__sal * months}'

class contractEmployee(Employee):
    __hr_pay : int = 300
    def salCal(self, hrs : int):
        return f'salCal for {hrs} hrs:{self.__hr_pay*hrs}'

pemp = perminentEmployee()
pemp.setName(fname="bhavya", sname="saranya", lname="25")
pemp.addAddress("venkatapuram")
print(pemp.getFullname())
print(pemp.getAddress())
print(pemp.salCal(10))

cemp = contractEmployee()
cemp.setName(fname="bhavya", sname="G", lname="saranya")
cemp.addAddress("venkatapuram")
print(cemp.getFullname())
print(cemp.getAddress())
print(cemp.salCal(10))

#multiple inheritence
class fName:
    def printName(self):
        print("Akhil")

class lName:
    def printName(self):
        print("varma")

class fullName(fName, lName):
    pass

a = fullName()
a.printName()

#hybrid inheritance

class fName:
    def printName(self):
        print("prasad")
class sName(fName):
    def printName(self):
        print("chinni")
class lName(fName):
    def printName(self):
        print("25")

class fullName(lName,sName):
    pass

b = fullName()
b.printName()