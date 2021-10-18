# class merupakan blue print dari objek
# objek memliki atribut dan behavior/method
class Hero:
    # Class of Variable, atribute/variable yang ada pada class
    # digunakan untuk class dan objek itu sendiri
    jumlah = 0
    # menggunakan method init, method ini dibuat saat instansiasi sebuah objek
    def __init__(self, inputName, inputEnergy, inputHealth, inputArmor):
        # varibale instance of object, variable yang hanya ada pada objek
        self.name = inputName
        self.energy = inputEnergy
        self.health = inputHealth
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Hero dengan nama "+inputName+" Telah dibuat")


# Membuat 4 objek dari satu bauh class
hero1 = Hero("Taufik", 100, 100, 50)
# Mencetak, dan memanggili variable jumlah dari class hero
print("Jumlah Hero adalah ", Hero.jumlah)
hero2 = Hero("Hakim", 90, 80, 60)
print("Jumlah Hero adalah ", Hero.jumlah)
hero3 = Hero("Rizki", 90, 100, 70)
print("Jumlah Hero adalah ", Hero.jumlah)
hero4 = Hero("Putra", 80, 75, 90)
print("Jumlah Hero adalah ", Hero.jumlah)
# Atribute Class Juga digunakan objek
print(hero1.jumlah)

# melihat data/atribut yang ada didalam objek
print(Hero.__dict__)








