class Hero:
    def __init__(self, namaInput, darahInput, armorInput):
        self.nama = namaInput
        self. __darah = darahInput
        self.__armor = armorInput
        # self.info = "nama {} , darah {}, armor {}".format(self.nama, self.__darah, self.__armor)
    # Ini adalah contoh encasupalsi, ini merupakan method getter untuk properti nama
    def getNama(self):
        return self.nama

    # property dapat mengubah function menjadi properti
    @property
    def info(self):
        return "nama {} , darah {}, armor {}".format(self.nama, self.__darah, self.__armor)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
nana = Hero("nana", 90, 80)

print(nana.getNama())
nana.nama = "nana1"
print(nana.info)
print(nana.armor)
