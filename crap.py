#!/usr/bin/env python3
import point


class Employee:
    'hahahaha'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Za", 2000)
emp2 = Employee("Ma", 5000)



class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)

    def myMethod(self):
        print("Calling parent method")



class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

    def myMethod(self):
        print('Calling child Method')


#c = Child()
#c.childMethod()
#c.parentMethod()
#c.setAttr(200)
#c.getAttr()
#c.myMethod()



class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)

print(v1 + v2)

