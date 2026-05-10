"""
Encapsulation: We are hiding the data into single unit. We can provide security to the variables,
(attributes)/functions.
Public: Type--> No underscore -->It can be accessible within the class/ Outside class/ subclasses
Private: Type--> __double underscore --> Only can be accessible within the class and it's child classes
Protected:Type--> _single underscore --> This can be access within the class, child class,
and outside of the class with object reference.
Private we can access outside of the class by using name mangling.



"""

class Employee:
    _place = "Bangalore" # protected variable
    def __init__(self, name, salary, emp_id, emp_email):
        self.name = name  #instance attribute, public variables
        self.salary = salary
        self.__emp_id = emp_id # private variable
        self._emp_email = emp_email # protected variable


        # public method, it can be accessible in any where , outside of the class, child class etc.
    def get_emp_details(self):
        print(self.name, self.salary)

    def get_salary(self):
        print(self.salary)

    def __get_salary_hike(self):
        print((self.salary/100)*5)

class Dept(Employee):
    __design = "QA Eng"
    def get_dept_details(self):
        print(self.name, self._emp_email)

# obj = Employee("Nandha", 30000, 123, "nandhu2gmail.com")
obj = Dept("Nandhu", 40000, 143, "nandhana@gmail.com")
# print(obj.get_emp_details())
print(obj.get_dept_details())
# print(obj.name, obj.salary, obj._emp_email)
print(obj._Employee__emp_id) # name mangling
print(obj._Dept__design)
obj.get_salary()
obj._Employee__get_salary_hike()
