# Membuat Variable Private
# Untuk Mengambil data menggunakan Getter
# Untuk men set data menggunakan Setter
class Hero:
    def __init__(self, inputNama, inputPower, inputDarah):
        self.__nama = inputNama
        self.__power = inputPower
        self.__darah = inputDarah

    # getter untuk mengambil nama
    def getNama(self):
        return self.__nama

    def getDarah(self):
        return self.__darah

    def diserang(self, damage):
        self.__darah -= damage

# awal dari game
batman = Hero("Taufik", 70, 75)


# Ketika Game Berjalan 
print(batman.__dict__)

# Karena Private, Varible tidak akan berubah
batman.__nama = "Rizki"

print(batman.getNama())

# Penggunaan setter untuk mengubah value pada variable object
batman.diserang(10)

print(batman.getDarah())