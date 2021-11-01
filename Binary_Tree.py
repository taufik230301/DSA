class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def add_child(self, data):
        # jika data sudah ada, maka return data
        if self.data == data:
            return data

        # cek apakah data lebih besar, maka isi ke child right dari root
        if self.data < data:
            # jika value child right sudah ada maka lanjutkan ke child left berikutnya
            if self.right:
                self.right.add_child(data)
            else:
                # jika value child right kosong maka, isi value terebut ke child right
                self.right = BinaryTree(data)

        elif self.data > data:
               # jika value child left sudah ada maka lanjutkan ke child left berikutnya
            if self.left:
                self.left.add_child(data)
            else:
                # jika value child right kosong maka, isi value terebut ke child right
                self.left = BinaryTree(data)

    # in order left, root, right
    def inorder_traversal(self):
        # Siapkan List Kosong
        element = []
        
        # 
        if self.left:
            element += self.left.inorder_traversal()
        
        element.append(self.data)

        if self.right:
            element += self.right.inorder_traversal()

        return element

           # Post order left, right, noded
    def post_order(self):
        # Siapkan List Kosong
        element = []

        if self.left:
            element += self.left.post_order()
        
        if self.right:
            element += self.right.post_order()

        element.append(self.data)

        return element

           # pre order root, left, right
    def pre_order(self):
        # Siapkan List Kosong
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.post_order()
        
        if self.right:
            element += self.right.post_order()

        return element
    

def build_tree(element):

    root = BinaryTree(element[0])

    for i in range(1, len(element)):
        root.add_child(element[i])
        
    return root

exercise = build_tree([3, 1, 7])

print(exercise.inorder_traversal())
print(exercise.post_order()) 
print(exercise.pre_order())       