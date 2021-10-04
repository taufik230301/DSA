# class merupakan blue print dari objek
# objek memliki atribut dan behavior/method
class Hero:
    pass

# Membuat Objek instance dari class
hero_1 = Hero()
hero_2 = Hero()
# Menambahkan atribut nama ke objek hero
hero_1.nama = "Taufik"
hero_2.nama = "Hakim"
hero_1.health = 100
hero_2.health = 300

# mencetak atribut nama dari tiap2 objek
print(hero_1.nama)
print(hero_2.nama)
print(hero_2.health)
print(hero_1.health)

# mencetak keterangan data yang ada didalam objek
print(hero_2.__dict__)