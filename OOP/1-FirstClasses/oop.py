class Employee:
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@email.com'
    self.pay = pay

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

emp1 = Employee('Thien', 'Kieu', 200000)
emp2 = Employee('Kieu', 'Thien', 400000)

print(emp1.fullname())
print(emp1.pay)
print(emp2.fullname())
print(emp2.pay)