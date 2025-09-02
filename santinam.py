class Sancho:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'my friend is {self.name}, hi is {self.age} age'
sancho = Sancho('Santina', 17)
print(sancho)