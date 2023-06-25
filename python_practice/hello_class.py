class Person:
    def __init__(self, name, age, greeting):
        self.name = name
        self.age = age
        self.greeting = greeting
    
    def personalGreeting(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        print(f'My favorite greeting is "{self.greeting}". Nice to meet you!')

myKid1 = Person("Izzy", 5.5, "Sup Dawg")
mykid2 = Person("Addy", 3, "I love you mommy")

print(myKid1.name)
print(myKid1.greeting)
mykid2.personalGreeting()
myKid1.personalGreeting()