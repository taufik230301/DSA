class Hero:
# Private variable
    __jumlah = 0

    def __init__(self, namaInput, darahInput):
        self.nama = namaInput
        self.darah = darahInput
        Hero.__jumlah +=1

    # method ini hanya terikat pada objek
    def getJumlah(self):
        return self.nama

    # Method ini hanya terikat pada class
    def getJumlah3():
        return Hero.__jumlah

    # Method yng terikat pada objek dan class
    # Tidak Perlu Menggunakan Properti Yang Ada pada Class
    @staticmethod
    def getJumlah1():
        return Hero.__jumlah

    # methof yang terikat pada class
    # Bisa Menggunakan Properti Yng ada pada class
    @classmethod
    def getJumlah2(cls):
        return cls.__jumlah
        

lina = Hero("lina", 100)
print(lina.getJumlah())
print(Hero.getJumlah3())
franko = Hero('Frankko', 90)
print(Hero.getJumlah1())
print(Hero.getJumlah2())

print(Hero.__dict__)
