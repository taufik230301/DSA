# Array dua dimensi biasa disebut array di dalam array

# Contoh pembuatan array dua dimensi 
from array import *

Array_2D = [[1, 2, 3, 4], [5, 6 ,7, 8], [9, 10, 11, 12]]
print(Array_2D[0])
print(Array_2D[0][1])
print(100*"#")

# Cara memasukan nilai ke Array 2D
Array_2D.insert(0, [0, 0, 0, 0])
print(Array_2D)

# Cara traverse Array 2D
for i in Array_2D:
    for n in i:
        print(n, end= " ")
    print()
print(100*"#") 

# Cara Update Array 2D
Array_2D[0] =[2, 3, 4, 5]
for i in Array_2D:
    for n in i:
        print(n, end=" ")
    print()

print(100*"#")
# Cara menghapus salah satu atau seluruh Array yang ada didalam array
del Array_2D[3]
for i in Array_2D:
    for n in i:
        print(n, end=" ")
    print()

