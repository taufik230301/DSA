
# Implementasi Dictionary
dict_1 = {'Maret 1': 'Taufik', 'Maret 2':'Kresna', 'Maret 3': 'Amin'}

# Mecetak Dictionary di Element Secara Spesifik
print(dict_1['Maret 1'])

# Cara mengupdate 
dict_1['Maret 1'] = 'Rangga'

print(dict_1)

# Menghapus dictionary pada lement secara spesifik, dan mengembalikan nilai nya
print(dict_1.pop('Maret 1'))
print(dict_1)

# Membuat Dict Baru
dict_2 = {'Maret 1': 'Taufik', 'Maret 2':'Kresna', 'Maret 3': 'Amin'}

# menghapus key and value dari dict, dan mengembalikan nilai nya
print(dict_2.popitem())
print(dict_2)

# Membersihkan Dictionary
dict_1.clear()
print(dict_1)

# # Menghapus Dictionary
# del dict_2
# print(dict_2)

# Memmasukan List ke dadalam Dict, dan membuat key dari index yang ada pada list, 
list_1 = ['Taufik', 'Dimas', "Angga"]
dict_3 = {}
for i in range(len(list_1)):
    dict_3[i] = list_1[i]
print(dict_3)

# Membuat Dict Mudah
# Membuat index otomatis menggunakan value 0
marks = {}.fromkeys(['Taufik', 'Dimas', 'Agil'], 0)
print(marks)
