class Employee:
  
  raise_amount = 1.04
  nums_of_emp = 0

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@email.com'
    self.pay = pay
    Employee.nums_of_emp += 1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Thien', 'Kieu', 200000)
emp2 = Employee('Kieu', 'Thien', 400000)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp1.raise_amount)

print(emp1.__dict__)
print(Employee.__dict__)

emp1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.nums_of_emp)