# Membatasi Instansiasi class hanya pada satu objek, melibatkan satu kelas untuk membuat method dan objek yang spesifik

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton("Deafult", 20)
        return Singleton.__instance

    def __init__(self, nama, umur):
        if Singleton.__instance != None:
            raise Exception("Objek ini Singleton!")
        else:
            self.nama = nama
            self.umur = umur
            Singleton.__instance = self

    def print_data(self):
        print(self.nama, self.umur)

a = Singleton("Taufik", 20)
# Membuat instance objek baru akan raise Execption "Objek ini Singleton"
# a = Singleton()
a.print_data()
print(a)
b = Singleton.getInstance()
c = Singleton.getInstance()
c.nama = a.nama
print(c.nama)
print(b.nama)