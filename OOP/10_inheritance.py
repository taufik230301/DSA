class Kendaraan:
    def __init__(self, namaInput, kecepatanInput):
        # Semua atribut atau method yang ada pada class ini dapat di akses, tapi method atau atribut yang ada pada kelas turunan
        # Tidak bisa diakses
        # Hanya bisa di akses disini, di class ini
        self.__nama = namaInput
        self.kecepatan = kecepatanInput

    def getNama(self):
        # Method ini bisa mengakses nya
        return self.__nama

class Mobil(Kendaraan):
    # Semua Atribut atau method yang ada pada class induk dapat di akses
    def __init__(self, namaInput, kecepatanInput, produksiInput):
        self.produksi = produksiInput
        Kendaraan.__init__(self, namaInput, kecepatanInput)
    # Karena Private Hanya bisa diakses oleh class itu sendiri, jadi class turunan tidak bisa mengakses variable private
    def getNamaMobil(self):
        return self.__nama

kendaraan = Kendaraan("Kendaraan", 100)
yamaha = Mobil("Mobil", 100, "Yamaha")


print(yamaha.getNama())

print(kendaraan.__dict__)

# Akan mengembalikan Variable nama
print(kendaraan.getNama())

# Tidak dapat mengembalikan variable nama karena private tidak dapat diakses dari luar maupun kelas turunan 
# # print(yamaha.getNamaMobil())
print(yamaha.produksi)

print(yamaha.__dict__)



