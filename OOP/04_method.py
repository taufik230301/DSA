class Hero:
    jumlah = 0
    def __init__(self, inputNama, inputDarah, inputArmor, inputKekuatan):
        self.nama = inputNama
        self.darah = inputDarah
        self.armor = inputArmor
        self.kekuatan = inputKekuatan
        Hero.jumlah +=1
        print("Ini adalah hero", self.nama)
        
# Membuat Method untuk Objek Dapat menyerang
    def meneyerang(self, lawan):
        print("Hero", self.nama, "Menyerang", lawan.nama)
        print("Hero", self.nama, "Menyerang Dengan Kekuatan", self.kekuatan)
        # Menggunakan kekuatan objek untuk mengurangi darah lawan
        lawan.darah -= self.kekuatan
        # lawan menggunakan method diserang, yang mana objek self menjadi objek yang menyerang, dan argument lawan.darah
        # untuk mengetahui darah lawan
        lawan.diserang(self, lawan.darah)

# masukan argument lawan sebagai objek yang memberikan perlawanan dan darah untuk mengetahui darah objek yang diserang
    def diserang(self, lawan, darah):
        # Hero objek self diserang hero objek lawan
        print("Hero", self.nama, "Diserang", lawan.nama)
        # Darah hero diakses dari varibale darah
        print("Darah Hero", self.nama, "Sekarang adalah", darah)


hero1 = Hero("Taufik", 100, 80, 5)
print("ini adalah hero ke -", Hero.jumlah)
hero2 = Hero("Hakim", 100, 90, 5)
print("ini adalah hero ke -", Hero.jumlah)
# ketika hero1 menggunakan method menyerang, dan harus di isi dengan objek yang akan diserang
hero1.meneyerang(hero2)
print(10*"#")
hero1.meneyerang(hero2)
print(10*"#")
hero1.meneyerang(hero2)
print(10*"#")
hero2.meneyerang(hero1)


    