# class Car:
#     # Store_name="The Great Valley" class attribute
#     #default constructor
#     def __init__(self):
#         pass

        
#     #constructor is exceuted when the object is being intilized
#     #parameter constructor
#     def __init__(self,color,brand):
#         self.color=color
#         self.brand=brand

# #instance means creating an object 
# c1=Car("black","Mercedes")
# print(c1.color,c1.brand)
# print(c1.Store_name)

from abc import ABC,abstractmethod
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @abstractmethod
    def get_avg_marks(self):
        return sum(self.marks)//len(self.marks)

    @staticmethod    #decorator
    def printMessage():
        print("Hello printing static method ")


# s1=Student("Abhishek",[100,99,100])
# print(s1.get_avg_marks())
# s1.printMessage()



#static method are those methd which dont use self parameter


# class Account:
#     def __init__(self,balance,account_no,passw):
#         self._balance=balance
#         self._account_no=account_no
#         self.__passw=passw  #private attribute 

#     def credit(self,amount):
#         if amount >0:
#             self._balance +=amount
#         else:
#             raise ValueError

#     def debit(self,amount):
#         if amount>0 and self._balance > amount:
#             self._balance -=amount
#         else:
#             raise ValueError

#     def checkBalance(self):
#         print(f"your {self._account_no} balance is {self._balance}")

#     def infoAccount(self):
#         return f" your account number {self._account_no} and password is {self.__passw}"


# a1=Account(1000,1234,"abhsillle")
# a1.checkBalance()
# a1.credit(2000)
# a1.debit(100)
# a1.checkBalance()
# a1.infoAccount()
# print(a1.__passw)




#Inheritance
#Single InheritanceOne child class inherits from a single parent class.A -> B
#Multiple InheritanceOne child class inherits from more than one parent class.A, B -> C
#Multilevel InheritanceA child class inherits from a parent, which in turn inherits from another parent.A -> B -> C
#Hierarchical InheritanceMultiple child classes inherit from a single parent class.A -> B and A -> C
#Hybrid InheritanceA combination of two or more types of inheritance mentioned above.Mixed
# class A:
#     def greet(self): print("Hello from A")

# class B(A):
#     def greet(self): print("Hello from B")

# class C(A):
#     def greet(self): print("Hello from C")

# class D(B, C):
#     pass
# class Car:
#     def __init__(self,carName,brand,color):
#         self.carName=carName
#         self.brand=brand
#         self.color=color

#     # @staticmethod
#     def start(self):
#         print(f"{self.carName} started")

#     @staticmethod
#     def stop():
#         print("Car stopped")


# class Maruti(Car):
#     def __init__(self, typ):
#         super().__init__(carName, brand, color)



# c1=Maruti("Maruti 800CC")
# c2=Maruti("Maruti Wagnor") 

# c1.start()


class Student:
    def __init__(self,phy,math,geo):
        self.phy=phy
        self.math=math
        self.geo=geo
        # self.percentage=str((self.phy+self.math+self.geo)/3)+ "%"

    # def calculatePercentage(self):
        # return str((self.phy+self.math+self.geo)/3)+ "%"
    
    #to use property ,when attribute behave like function ,then make a function for that attribute this can update the % 
    @property
    def percentage(self):
        return str((self.phy+self.math+self.geo)/3)+ "%"
        

# s1=Student(98,97,99)
# print(s1.percentage)


# s1.phy=86
# print(s1.phy)
# # print(s1.calculatePercentage())
# print(s1.percentage)

#decorator-> staticmethod ,classMethod,property,getter,setter

#Polymorphism -> when same operator can be allowed to have different meaning according to context (operator overloading)


#reference 3.3.8 -> https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

# class Circle:
#     def __init__(self,radius,PIE=3.14):
#         self.radius=radius
#         self.PIE=PIE

#     def area(self):
#         return self.PIE*self.radius**2

#     def perimeter(self):
#         return 2*self.PIE*self.radius

# c1=Circle(10)
# print(c1.area())
# print(c1.perimeter())


class Employee:
    def __init__(self,role,department,salary:int):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        return f"{self.role} working in this {self.department} with salary of {self.salary}"

class Engineer(Employee):
    def __init__(self,name,age,role, department, salary):
        super().__init__(role, department, salary)
        self.name=name
        self.age=age

    def printInfo(self):
        print(f"{self.name} role is {self.role} working in this {self.department} with salary of {self.salary}")

# e_1=Employee("Software Engineer","Ecommerce",90000)
# print(e_1.showDetails())
e1 = Engineer("Jagdish",29,"Software Engineer","Ecommerce",90000)
print(e1.printInfo())