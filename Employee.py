class Employee:
    def __init__(self, name, address, code, salary):
              self.name= name
              self.address=address
              self.name= address
              self.code= code
              self.salary=salary
              
    def __str__(self):
             return f'{self.name},{self.address},{self.code},{self.salary}'
         
mahesh= Employee('patilram','pune','PYAB10021',20000)
print(mahesh)