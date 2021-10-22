from Karyawan import Karyawan 
# Class KayawanFactory dapat membuat objek dari kelas karyawan, karena tujuan dari design pattern ini adalah
# Memungkinkan class atau interface membuat objek dari suatu kelas
# client menggunakan class atau interface tertentu untuk membuat instance objek
class KaryawanFactory:
    
    @staticmethod
    def createManager(nama):
        return Karyawan(nama, 'Manager', 10000000)

    @staticmethod
    def crateStaff(nama):
        return Karyawan(nama, 'Staff', 2000000)