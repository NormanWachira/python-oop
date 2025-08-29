# This Program contains Encapsulation(private attributes, getters and setters), Inheritance and Polymorphism altogether

# Activity 1

# Base class 'Employee'
class Employee:
    def __init__(self, name, salary, role):
        # Private attributes
        self.__name = name;
        self.__salary = salary;
        self.__role = role;

    # getter for name
    @property
    def name(self):
        return self.__name;
    # getter for salary
    @property
    def salary(self):
        return self.__salary;
    # setter for salary
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value;
        else:
            raise ValueError("Salary must be non-negative");
    # getter for role
    @property
    def role(self):
        return self.__role;

    # Another method 'Work'
    def work(self):
        return "Working";

# class Inheritances
class Teacher(Employee):
    def work(self):
        return "Teaching students";

class Chef(Employee):
    def work(self):
        return "Cooking meals";

class Driver(Employee):
    def work(self):
        return "Driving passengers";


# Objects and Polymorphism in action in the work() methods

t=Teacher("Abraham", 5000, "Farmer")
c=Chef("Benjamin", 4000, "Chef")
d=Driver("Norman", 30000, "Engineer")

employees=[t,c,d]

for emp in employees:
    print(f"Name: {emp.name} | Role: {emp.role} | Work: {emp.work()} | Salary: ${emp.salary}")

