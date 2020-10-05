class Employee():

    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email = first + "." +last+ "@gmail.com"

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt = amt

    @classmethod
    def from_strin(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        return True



class Developer(Employee):
    raise_amt = 1.03
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def app_employee(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def show_employees(self):
        for emp in self.employees:
            print(emp.fullname())

emp_1 = Employee('Maciej',
                 'Janowski',40000)


print(emp_1.fullname())


dev_1 = Developer('Karol','Kowalik',100000,'Python')
dev_2 = Developer('Magdalena','Walka',123400,'Java')
# print(emp_1.pay)
# print((emp_1.apply_raise()))
# print(emp_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)



Employee.set_raise_amt(1.09)
print(emp_1.raise_amt)
print(Employee.raise_amt)

import datetime

my_date = datetime.date(2016,1,11)
print(Employee.is_workday(my_date))


mgr_1 = Manager('Maciej','Janowski',200,[dev_1])

mgr_1.app_employee(dev_1)
mgr_1.show_employees()

mgr_1.add_employee(dev_2)
mgr_1.show_employees()



