class Stack:
    def __init__(self):
        # Membuat stack dengan menggunakan list
        self.stack = []

    def push_value(self, data):
        # Cek jika data tidak ada di dalam stack maka masukan
        if data not in self.stack:
            # Jika data yang dimasukan sama denga value yang ada didalam stack maka return false, jika tidak
            # Maka masukan data
            self.stack.append(data)
            return True
        else:
            return False

    # Melihat element terakhir dari stack
    def peek(self):
        return self.stack[-1]

    def print_value(self):
        return self.stack

# Cara pop, mengeluarkan element terakhir dari stack
    def pop_value(self):
        # Cek jika stack kosong, maka jangan pop
        if self.stack is None:
            print("stack is empty")
        else:
            return self.stack.pop()


stack = Stack()
stack.push_value("1")
stack.push_value("2")
stack.push_value("3")
stack.push_value("4")
stack.push_value("5")

print(stack.print_value())

print(stack.peek())

print(stack.pop_value())
print(stack.print_value())
        
            




