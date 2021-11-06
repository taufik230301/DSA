# Membuat Furnitur
# Membuat Furnitur memiliki dua objek yaitu Meja dan Kursi
# Dimana Meja dan kursi memiliki dua tipe, yaitu meodern dan classic
# Jadi dari dua objek masing masing memiliki dua tipe

# Class furnitur sebagai abstract class
class Furnitur:
    __furnitur = ""
    __harga = ""

    def __init__(self, furnitur, harga):
        self.__furnitur = furnitur
        self.__harga = harga

    # Buat fungsi untuk mengambil harga dari objek
    def getHarga(self):
        return self.__harga

    # Buat fungsi untuk mengambil nama dari objek
    def getFurnitur(self):
        return self.__furnitur


# Buat 4 class untuk tiap tiap objek
class MejaModern(Furnitur):
    def __init__(self):
        Furnitur.__init__(self, "Meja Modern", "90000")

class MejaCLassic(Furnitur):
    def __init__(self):
        Furnitur.__init__(self, "Meja Classic", "80000")

class KursiModern(Furnitur):
    def __init__(self):
        Furnitur.__init__(self, "Kursi Modern", "70000")

class KursiCLassic(Furnitur):
    def __init__(self):
        Furnitur.__init__(self, "Kursi Classic", "50000")


# Buat class Factory untuk membuat objek
class FurniturFactory:
    def getFurniturModern(self): pass
    def getFurniturClassic(self): pass

# Class Meja Factory untuk membuat objek meja
class MejaFactory(FurniturFactory):
    # Fungsi untuk membuat objek meja bertipe Modern
    def getFurniturModern(self):
        return MejaModern()
    # Fungsi untuk membuat objek meja bertipe Classic
    def getFurniturClassic(self):
        return MejaCLassic()

class KursiFactory(FurniturFactory):
    # Fungsi untuk membuat objek kursi bertipe Modern
    def getFurniturClassic(self):
        return KursiCLassic()
    # Fungsi untuk membuat objek kursi bertipe Classic
    def getFurniturModern(self):
        return KursiModern()

mfactory = MejaFactory()
kfactory = KursiFactory()

meja = mfactory.getFurniturClassic()
print(meja.getHarga())
kfactory = KursiFactory()


kursi = kfactory.getFurniturClassic()
print(kursi.getFurnitur())


    