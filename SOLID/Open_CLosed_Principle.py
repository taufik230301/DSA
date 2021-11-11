# Class, Modulue and Function harus Open dengan adanya extension bukan modfication

class Animal:
    def __init__(self, nama):
        self.nama = nama

    def get_name(self):
        return self.nama

animals = [
        Animal('lion'), 
        Animal('cat')
        ]

# Kelas ini menyalahi aturan open Closed Principle, karena function ini open terhadap medifikasi bukan extension
# Jika client menambahkan objek baru dari class animal, maka harus memodifikasi function tersebut   
def animal_make_sound(animals: list):
    for animal in animals:
        if animal.nama == "lion":
            print("roar")
        elif animal.nama == "cat":
            print("cat")

animal_make_sound(animals)





    