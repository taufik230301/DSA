from Animal import Animal, Tiger, Cat, Cow

class AnimalFactory:

    @staticmethod
    def create_animal(kategori):
        if(kategori == "tiger"):
            return Tiger()
        elif(kategori == "cat"):
            return Cat()
        elif(kategori == "cow"):
            return Cow()