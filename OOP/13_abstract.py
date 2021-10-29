class Animal:

    def speak(self):
        pass


class Tiger(Animal):
    def speak(self):
        return "GHAHAA!"


class Cat(Animal):
    def speak(self):
        return "MEOWW!"


tiger = Tiger()
print(tiger.speak())


cat = Cat()
print(cat.speak())