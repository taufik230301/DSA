# Cara membuat list
# List mutable(dapat di modidikfasi dan di update nilai nya)
# Value yang ada dalam List bisa terdapat dua tipe data atau lebih
list1 = ['fisika', 'matematika', 'biologi']

# Cara mencetak list
print("# Cara mencetak list")
print(list1)

# Untuk menghitung panjang dari sebuah list
lenght1 = len(list1)
print(lenght1)

# Mengakses value pada list menggunakan index pada list
print("list1[0] : ", list1[0])

print("list1[1:5]", list1[1:5])

# Mengupdate value pada list menggunakan index pada list
list1[0] = "sejarah"

print(list1)

# Menghapus salah satu value list menggunakan index
del list1[1]
print(list1)

# Menambah Value List Di Akhir Element
list1.append("kimia")

for x in list1:
    print(x)

list_3 = ['a', 'b', 'c']

# Menambah Value di elemen tertentu
list_3.insert(0, 'a')
print(list_3)

list_4 = [9, 4, 1, 7, 8]
# Untuk mengurutkan elemen pada list
list_4.sort()

print(list_4)

# Untuk mengeluarkan elemen terakhir dari sebuah list
list_4.pop()
print(list_4)

list_5 = [4, 5, 6, 1, 2, 7]
# Untuk membalikan list
list_5.reverse()
print(list_5)

# Perintah Untuk Meremove List dari value tertentu
list_5.remove(7)
print(list_5)
