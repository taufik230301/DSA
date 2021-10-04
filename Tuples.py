# Tuples immutable(tidak dapat dimodifikasi atau di update nilainya), berbeda dengan list
# Value yang ada didalam tuple bisa terdapat dua tipe data atau lebih

tup = ('taufik', 'kresna', 'jalal', 1, 2)
tup1 = ('Deak', 'Azahra', 'Kiki')

print(tup)

# Cara mengakses tuple
print("tup[0] : ", tup[0])
print("tup[0:2]", tup[0:2])

# Membuat tuple baru dari beberapa tuple
tup2 = tup + tup1
print(tup2)

# salah satu nilai tuple tidak dapat dihapus, tetapi tuple dapat dihapus secara keseluruhan
del tup2
print(tup2)