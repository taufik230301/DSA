class Hero:
    def __init__(self, namaInput, darahInput):
        self.nama = namaInput
        self.darah = darahInput

class Hero_Tank(Hero):
    pass

franko = Hero_Tank("franko", 100)

print(franko.__dict__)
print(Hero.__dict__)
print(Hero_Tank.__dict__)