from Karyawan import Karyawan 

class KaryawanFactory:
    
    @staticmethod
    def createManager(nama):
        return Karyawan(nama, 'Manager', 10000000)

    @staticmethod
    def crateStaff(nama):
        return Karyawan(nama, 'Staff', 2000000)