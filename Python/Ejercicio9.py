"""
Ejercicio
"""

class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):

        def sound(self):
            print("Woof!")

class Cat(Animal):
        def sound(self):
            print("Meow!")

def print_sound(animal: Animal):
    animal.sound()

my_dog = Dog("Rex")
print_sound(my_dog)
my_cat = Cat("Whiskers")
print_sound(my_cat)

"""
Extra
"""

class Employee:
        def __init__(self, id: int, name:str):
            self.id = id
            self.name = name
            self.employees = []

        def add(self, employee):
            self.employees.append(employee)

        def print_employees(self):
            for employee in self.employees:
                print(employee.name)

class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa")

class ProjectManager(Employee):
    def __init__(self, id: int, name:str, project:str):
        super().__init__(id, name)
        self.project = project

    def coordinate_projects(self):
        print(f"{self.name} está coordinando su proyecto")

class Developer(Employee):
    def __init__(self, id: int, name:str, language:str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}")

    def add(self, employee: Employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá")

my_manager = Manager(1, "Sinsinati")
my_project_manager = ProjectManager(2, "Sergio", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Antonio", "Proyecto 2")
my_developer = Developer(4, "Giacomo", "Python")
my_developer2 = Developer(5, "Andrea", "Cobol")
my_developer3 = Developer(6, "Susana", "Swift")
my_developer4 = Developer(7, "Gloria", "Dart")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_developer)
my_project_manager.add(my_developer2)
my_project_manager2.add(my_developer3)
my_project_manager2.add(my_developer4)

my_developer.add(my_developer2)

my_developer.code()
my_project_manager.coordinate_projects()
my_manager.coordinate_projects()

my_manager.print_employees()
my_project_manager.print_employees()
my_developer.print_employees()