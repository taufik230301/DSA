class Hero:
    def __init__(self, namaInput, darahInput, kekuatanInput):
        self.__nama = namaInput
        self.__darah = darahInput
        self.__kekuatan = kekuatanInput

    # Kita akan membuat setter
    # Buat def property agar atribut private dapat di akses
    @property
    def info(self):
        return "nama {}, darah {}, kekuatan {}". format(self.__nama, self.__darah, self.__kekuatan)

    @property
    def darah(self):
        pass

    # Membuat setter untuk, mengupdate data dari variable private
    @darah.setter
    def darah(self, input):
        self.__darah = input
    


zoyun = Hero("Zoyun", 90, 80)
print(zoyun.info)
zoyun.darah = 100
print(zoyun.__dict__)
