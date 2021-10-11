# Tree terdiri dari parent child, satu parent dapat memiliki banyak child
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

root = Tree("Barang_elektronik")

laptop = Tree("Laptop")
laptop.add_child(Tree("HP"))
laptop.add_child(Tree("samsung"))
laptop.add_child(Tree("Apple"))

mobil = Tree("Mobil")
mobil.add_child(Tree("Suzuki"))
mobil.add_child(Tree("Hyundai"))
mobil.add_child(Tree("Yamaha"))



root.add_child(laptop)
root.add_child(mobil)

root.print_all()




    