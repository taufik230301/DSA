class Hero:
    def __init__(self, inputNama, inputDarah, inputKekuuatan, inputPertahanan):
        self.nama = inputNama
        self.darah = inputDarah
        self.__kekuatan = inputKekuuatan
        # protected Variable Bisa digunakan di class dan class turunanan nya
        # Tapi protected tidak bisa diakses dari luar class atau dari luar class turunannya
        self._pertahanan = inputPertahanan
    
    def tambahDarah(self):
        # Private Variable hanya bisa digunakan di dalam class
        self.darah += self.__kekuatan + 5
        return self.darah


hero1 = Hero(100, 80, 5, 80)

darahPertama = hero1.tambahDarah()
hero1.tambahDarah()
print(darahPertama)
print(hero1.darah)

hero1._pertahanan = 90
print(hero1.__dict__)
# Tidak dapat mengakses Private Varible diluar class
hero1.__kekuatan



