class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Person:\tname {self.name} age {self.age}')


p = Person('Ivan', 21)
p.print_info()
