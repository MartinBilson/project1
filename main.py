class Person:
    def __init__(self, name, career):
        self.name = name
        self.career = career

    def __str__(self):
        return f"My name is {self.name} and my career is {self.career}"
    
p1 = Person("Martin Githae", "Software Engineer")

print(p1)