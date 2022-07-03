"""
Clases, metodo constructor, super y polimorfismo

15/07/2021
"""

class Person():
    def __init__(self, name, lastName, genre):
        self.name = name
        self.lastName = lastName
        self.genre = genre

    def describe(self):
        print(f"Name: {self.name}, {self.lastName}  - Genre: {self.genre}")

    def say_hello(self):
        print(f"Hello {self.name}")

class Employ(Person):
    def __init__(self, name, lastName, genre, position, salary, entryJob):
        super().__init__(name, lastName, genre)
        self.position = position
        self.salary = salary
        self.entryJob = entryJob

    def describe(self):
        #super().describe() # Esto permite llamar a la funcion superior
        print(f"Position: {self.position}  - Salary: {self.salary}  - Date Entry: {self.entryJob}")

def describeTotal(personEmp): # Polimorfismo
    personEmp.describe()

def say_something(sayPerson):
    sayPerson.say_hello()

person1 = Person("Eddie", "Espinoza", "M")
person1.describe()
employ1 = Employ("Eddie", "Espinoza", "M", "Developer", 150_000, "01/01/2021")
employ1.describe()
print("Polimorfismo")
describeTotal(person1)
say_something(person1)
