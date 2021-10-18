class Hero:
    hitung = 0
    def __init__(self, namaInput, darahInput):
        self.__nama = namaInput
        self.darah = darahInput
        Hero.hitung +=1

    def getnama1(self):
        return self.__nama
        
    @classmethod
    def getnama(self):
        # Tidak dapat mengakses instance variable, hanya dapat mengakses informasi atribut class variable
        return self.hitung

franko = Hero('Franko', 100)

print(Hero.getnama())
print(franko.getnama1())
