# Menangani collision pada hashtable
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    # Fungsi Hash, dimana nilai key yang akan ditambahkan, diproses didalam fungsi ini, untuk menentukan index ke berapa
    # pasangan key dan value ini di simpan
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    # 
    def __getitem__(self, key):
        # Ambil result hash dan simpan ke arr_index
        arr_index = self.get_hash(key)
        # periksa setiap item tuple yang ada didalam array
        for kv in self.arr[arr_index]:
            # Jika elemnt 0 tuple sama dengan key yang ingin di tampilkan datanya, maka tampilan data value dari 
            # key tersebut
            if kv[0] == key:
                return kv[1]

            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        # Cek tiap-tiap element yang ada dialam tuple
        for idx, element in enumerate(self.arr[h]):
            # jika panjang element tuple tersebut sama dengan dua, yang artinya sudah ada pasangan key dan value
            # dan elemnt 0 sama dengan key yang akan di set
            if len(element)==2 and element[0] == key:
                # maka update value lama dari key tersebut dengan value baru
                self.arr[h][idx] = (key,val)
                found = True
        # Jika tidak ada, maka tambahkan element tuple baru ke dalam array
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        # Delete berdasarkan key yang ingin didelete
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457


print(t["march 17"])
print(t.arr)