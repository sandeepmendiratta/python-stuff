#!/usr/bin/python

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + 'company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'new', 5000)
emp_2 = Employee('sand', 'old', 600)

#Employee.fullname(emp_1)
#emp_1.fullname()
#print(emp_1.fullname())
#print('{} {}'.format(emp_1.first, emp_1.last))
#print(Employee.fullname(emp_2))

print(emp_1.__dict__)
print(Employee.__dict__)
