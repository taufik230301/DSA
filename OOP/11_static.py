class Manusia:
    def __init__(self, nama):
        self.__nama = nama
    
    def getnama(self):
        return self.__nama

    @staticmethod
    def nama_besar(nama):
        return nama.upper()

class Laki(Manusia):
    def __init__(self, nama):
        super().__init__(nama)
    
    def getnama(self):
        return Manusia.nama_besar(super().getnama())

manusia_1 = Manusia("Taufik")

print(manusia_1.getnama())
# Static method dapat diakses dengan awalan class, static method menghiraukan informasi yang ada pada class/tidak 
# menggunakan atribut yang ada pada class
print(Manusia.nama_besar('Fadilah'))

laki_1 = Laki("Taufik_1")

print(laki_1.getnama())