class Karyawan:
    def __init__(self, namaInput, jabatanInput, gajiInput):
        self.__nama = namaInput
        self.__jabatan = jabatanInput
        self.__gaji = gajiInput

    def getNama(self):
        return self.__nama

    def getJabatan(self):
        return self.__jabatan

    def getGaji(self):
        return self.__gaji

# manager_1 = Karyawan('Taufiiqul Hakim', 'Manager 1', 100000)

# print(manager_1.getNama())