# Employee Management Program

This program demonstrates **Encapsulation, Inheritance, and Polymorphism** in Python using an `Employee` class and its subclasses.

## Features

- **Encapsulation**:  
  Private attributes (`__name`, `__salary`, `__role`) with **getters and setters** to safely access and modify data.  

- **Inheritance**:  
  Subclasses (`Teacher`, `Chef`, `Driver`) inherit common attributes and methods from the base `Employee` class.  

- **Polymorphism**:  
  Each subclass overrides the `work()` method to define its own behavior, demonstrating polymorphic behavior when iterating over a list of employees.

## Usage

1. **Create employee objects:**

```python
t = Teacher("Abraham", 5000, "Farmer")
c = Chef("Benjamin", 4000, "Chef")
d = Driver("Norman", 30000, "Engineer")
