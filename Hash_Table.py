# Implementasi Hash Table
class Hash_Table:
    def __init__(self):
        self.MAX = 50
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

t = Hash_Table()
t['Maret 6'] = 180
t['Maret 17'] = 100
print(t['Maret 6'])
print(t.arr)
