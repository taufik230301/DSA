from AnimalFactory import AnimalFactory

tiger = AnimalFactory.create_animal("tiger")
cow = AnimalFactory.create_animal("cow")
print(tiger.speak())
print(cow.speak())

