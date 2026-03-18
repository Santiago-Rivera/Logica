"""
Ejercicio
"""

class Programmer:

    surname: str = None

    def __init__(self, name:str, age:int, language:list):
        self.name = name
        self.age = age
        self.language = language

    def print ( self ):
        print(f"Name: {self.name} | Lastname: {self.surname} | Age: {self.age} | Language: {self.language}")

my_programmer = Programmer("John", 30, ["Python", "JavaScript"])
my_programmer.print()
my_programmer.surname = "Doe"
my_programmer.print()
my_programmer.age = 31
my_programmer.print()

"""
Extra
"""

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Stack count:", my_stack.count())
my_stack.print()
print("Popped item:", my_stack.pop())
print("Stack count after pop:", my_stack.count())
my_stack.print()

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
            print(item)

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print("Queue count:", my_queue.count())
my_queue.print()
print("Dequeued item:", my_queue.dequeue())
print("Queue count after dequeue:", my_queue.count())
my_queue.print()