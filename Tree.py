# Tree terdiri dari parent child, satu parent dapat memiliki banyak child
# Buat atribut parent, untuk menyimpan data parent nya
# Buat Atribut data, untuk menyimpan data dari tiap2 node
# Buat Atribut Childer untuk menyimpan data child dari tiap2 node parent
class Tree:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level+= 1
        return level

    def print_all(self):
        level = self.get_level()
        print('-'*level*2, self.data)
        if self.children:
            for child in self.children:
                child.print_all()

    def search(self, name):
        if self.data == name:
            print(self.data)
        c = self.children
        if c:
            
            for child in self.children:
                if child.data == name:
                    n = child
                    str_1 = ""
                    while n:
                        str_1 = n.data +' / '+str_1
                        n = n.parent
                    print(str_1)
                else:
                    child.search(name)
               

root = Tree("Barang_elektronik")

laptop = Tree("Laptop")
laptop.add_child(Tree("HP"))
laptop.add_child(Tree("samsung"))
laptop.add_child(Tree("Apple"))

mobil = Tree("Mobil")
mobil.add_child(Tree("Suzuki"))
mobil.add_child(Tree("Hyundai"))

yamaha = Tree("Yamaha")
yamaha.add_child(Tree("Yamaha 1"))
yamaha.add_child(Tree("Yamaha 2"))
yamaha.add_child(Tree("Yamaha 3"))

mobil.add_child(yamaha )



root.add_child(laptop)
root.add_child(mobil)

root.print_all()

root.search("HP")





    