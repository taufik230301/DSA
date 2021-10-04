# class merupakan blue print dari objek
# objek memliki atribut dan behavior/method
class Hero:
    # Class of Variable, objek yang ada pada class
    jumlah = 0
    # menggunakan method, method ini dibuat saat instansiasi sebuah objek
    def __init__(self, inputName, inputEnergy, inputHealth, inputArmor):
        # varibale instance of object, variable yang hanya ada pada objek
        self.name = inputName
        self.energy = inputEnergy
        self.health = inputHealth
        self.armor = inputArmor


# Membuat 4 objek dari satu bauh class
hero1 = Hero("Taufik", 100, 100, 50)
hero2 = Hero("Hakim", 90, 80, 60)
hero3 = Hero("Rizki", 90, 100, 70)
hero4 = Hero("Putra", 80, 75, 90)

# melihat data/atribut yang ada didalam objek
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)






