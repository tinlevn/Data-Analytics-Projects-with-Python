#PROJECT 2 CS443
#Major contributor is Jeremy, I helped with a third of the code and major comments/formatting. 
#Please read from include .txt on your machine for code to run.

from itertools import groupby
from math import inf
from collections import UserDict

class Employee:  
    empCount = 0  
    def __init__(self, name, salary, age):
        self.name = name      
        self.age = age
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee: {0}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name : {0}, Salary: {1}, Age: {2}".format(self.name,
                                                         self.salary,
                                                         self.age))
    #METHOD FROM SECOND QUESTION
    def work(self):
        print("Employee {0} works at the age of {1} for a salary of " \
              "${2:.2f}".format(self.name, self.age, self.salary))

#QUESTION 1                             
employees = [Employee(name='Morgan', age=23, salary=25000),
             Employee(name='Jeremy', age=21, salary=50000),
             Employee(name='Ally', age=2, salary=0),
             Employee(name='Ben', age=5, salary=17),
             Employee(name='Beth', age=17, salary=6000)]
 
top_three = sorted(employees, 
                   key=lambda employee: employee.salary, 
                   reverse=True)[:3]
print("First Question Output:")
for e in top_three:
    e.displayEmployee()
print()

#QUESTION 2
class Company:
    def __init__(self):
        self.employeeList=[]
    def addEmployee(self, employee):
        self.employeeList.append(employee)
    def work(self):
        for emp in self.employeeList:
            emp.work()

emp1 = Employee("Kevin", 2900, 29)
emp2 = Employee("Jose", 5000, 40)
emp3 = Employee("Ameer", 7000, 45)
emp4 = Employee("Jennifer", 800, 33)
emp5 = Employee("Sandre", 2550, 23)
employeeList = [emp1, emp2, emp3, emp4, emp5]
company = Company()
print("Second Question Output:")
for emp in employeeList:
    company.addEmployee(emp)
company.work()
print()

#QUESTION 3
#Display all employee function
def displayAllEmployee(list):
    for i in list:
        i.displayEmployee()
#Read line from a file that contains employee info
def readEmployee():    
    for line in open("D:/employeeinfo.txt"):
            employee= line.split()
            yield employee     
#Generator used for raising salary by 5%   
def raisesalary(employ):   
        for i in employ:
            yield int(i.salary) + int(i.salary) *.05
#Turning list into generator, returning employee object
def createDict(elist):
    for i in elist:
        yield i

#Return age range given an employee
def age_range(employee):
    age_ranges = [(0, 20),
                  (21, 30),
                  (31, 50),
                  (51, 65),
                  (65, inf)]
    for begin, end in age_ranges:
        if begin <= employee.age <= end:
            return begin, end

#Create list and append employees from reading from .txt file
employeelist=[]
print("Adding employees from file")
for i in readEmployee():
    employeelist.append(Employee(name=i[0],age=int(i[1]),salary=float(i[2])))
displayAllEmployee(employeelist)
print()

#Sort by name
print("Employee list with sorted names")
employeelist=sorted(employeelist, key=lambda x: x.name)
displayAllEmployee(employeelist)
print()

#Raise salary
print("Employee list with raised salaries")
for i, x in enumerate(raisesalary(employeelist)):
    employeelist[i].salary = x
displayAllEmployee(employeelist)
print()

#Create dictionary using generator and having keys' range in 10
print("Dictionary of employees created with keys ranging from 0-9/range(10)")
employee_dict={i: j for i,j in enumerate(createDict(employeelist))}
for keys,values in employee_dict.items():
    print(keys, end=": ")
    values.displayEmployee()

#Printing itertools' groupby age group for employee
print()
print("Age range and names:")
grouped_employeelist = groupby(sorted(employeelist, key=lambda x: x.age), key=age_range)
for key, x in grouped_employeelist:
    print(key, end=": ")
    print([e.name for e in x])
print()

#QUESTION 4
class EmployeeD(UserDict):
    def init(self):     
        self.data = {}
    def getitem(self, key):
        return self.data[key]
    def setitem(self, key, val):
        self.data[key] = val

def generator(file_name):
    lines = tuple(open(file_name))
    E=EmployeeD()
    for line in lines:
        words=line.split()
        E=EmployeeD()
        E['name']=words[0]
        E['salary']=words[2]
        yield E
print("ANSWER FOR QUESTION 4: PRINTING TOTAL SALARY OF ALL EMPLOYEES USING GENERATOR FUNCTION")
total=sum([int(E['salary']) for E in generator('D:/employeeinfo.txt')])             
print('Total Salary',total)
