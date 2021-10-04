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

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

t = Hash_Table()
t.add('Maret 6', 100)

print(t.arr)
