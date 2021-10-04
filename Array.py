from array import * 

array1 = array('i', [1, 2, 3, 4])

# Cara Insert Array
array1.insert(1, 1) 

# Cara Menghapus Array
array1.remove(2)    

# Cara Update Array
array1[0] = 0

array1.pop()

# Cara traverse array
for x in array1:
    print(x)

# Cara akses elemen dalam array
print(array1[0])

# Cara search array
print(array1.index(3))

# Mengeluarkan Element terakhir pada array
array2 = array('i', [1, 2, 3, 4])

array2.pop()

print(array2)

