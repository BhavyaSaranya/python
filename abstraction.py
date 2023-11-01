#example of abstraction

class Name:
    _firstName:str="bhavya"
    _lastName:str="saranya"
    def fullName(self):
        return self._firstName +" "+ self._lastName
emp=Name()
emp._lastName="Gottumukkala"
print(emp.fullName())

#variable scope wrt scope
#public scope

class Name:
    firstName:str="bhavya"
    lastName:str="saranya"
emp=Name()
print(emp.firstName)

#variable scope wrt to functions
#global variable scope

def fullName():
    global lName
    fName="bhavya"
    lName="saranya"
fullName()
print(lName)
print(fName)




