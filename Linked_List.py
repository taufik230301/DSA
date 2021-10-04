# Buat class Node untuk membuat object node pada linked list
class Node:
    def __init__(self, data=None, next=None, prev=None):
        # Deklarasikan variable data untuk menyimpan nilai didalam node 
        self.data = data
        # Deklarasikan variable next untuk menyimpan data.next dari node sebelumnya
        self.next = next
        # Deklarasi variable prev untuk menyimpan data.prev dari node setelahnya
        self.prev = prev

# Buat class List untuk membuat object list yang dimana object tersebut dapat menyimpan object node dari class node
class List:
    def __init__(self):
        # Deklarasikan variable head untuk menyimpan data head pada object list
        self.head = None
# Membuat function prinval untuk print nilai yang ada didalam list
    def printval(self):
        # Masukan nilai head ke dadalam variable prinval
        printval = self.head
        # Deklarasikan variable listdata untuk menyimpan data kedalam string kosong
        listdata = ""
        # Selama printval tidak none
        while(printval is not None):
            # masukan data kedalam listdata
            listdata += str(printval.data) + '-->'
            # print listdata
            
            # update ke next data
            printval = printval.next        
        print(listdata)

# Deklarasikan function insert_at_begining yang menggunakan satu parameter untuk menyimpan data
    def insert_at_begining(self, data):
        if self.head is not None:
        # Masukan data ke dalam class Node dan masukan ke Variable Newdata
            Newdata = Node(data)
        # Tetapkan Newdata.next menjadi self.head
            Newdata.next = self.head
        # Tetapkan self.data menjadi Newdata
            self.head = Newdata
        else:
            self.head = Node(data)

            # 2->4->9->9->0->null
            # head nya ditetapkan ke data baru, dan data baru nextnya itu ke head data lama
            # 8->2->4->9->9->0->null

    def insert_at_end(self, data):
        # Cek apakah head kosong
        if self.head is None:
            # Jika head kosong maka masukan nilai ke head
            self.head = Node(data, None)
        else:
        # jika head tidak none, tetapkan nilai ke variable Newdata
            Newdata = self.head
        # Selama Newdata.next tidak kosong maka, update Newdata.next ke next selanjutnya
            while(Newdata.next):
                Newdata = Newdata.next
        # Jika Newdata.next kosong, bererti iterasi telah mencapai akhir dari node, 
        # maka masukan nilai baru ke Newdata.next yang tidak ada isi
            Newdata.next = Node(data, None)

            # 2->4->9->9->0->null
            # Jika sudah mencapai tail, maka tetapkan 0 next ke data baru yang kita masukan
            # 2->4->9->9->0->8->null

# Insert Pada Poin tertentu
    def insert_at(self, index, data):
        # Cek apakah index kurang dari 0 atau index lebih dari panjang linked list
        if index < 0 or index > self.get_length():
            # Jika ya, Data Invalid
            raise Exception("Data Invalid")

        # Jika index sama dengan 0 maka jalankan fungsi insert at the begining
        if index == 0:
            return self.insert_at_begining(data)

        # Mulai hitung
        count = 0
        # node itr yang sekarang
        itr = self.head
        # Selama itr ada value maka terus berjalan
        while(itr):
            # Jika count sudah mencapai index - 1, damana node dari linked list sebelum nya
            if count == index -1:
                # masukan data ke dalam nya, dan node next dari linked list tersebut adalah node next dari linked list sebelumnya
                node = Node(data, itr.next)
                # Tetapkan node next dari linked list sebelum nya, ke data baru yang dimasukan
                itr.next = node
                # Jika sudah, maka program berhenti
                break
            # Jika count belum mencapai index -1 , maka lanjutkan iterasi
            itr = itr.next
            # Lanjutkan Juga perhitungan
            count+=1

            # 2->4->9->9->0->null
            # 2->4->9->9 (kita isi disini) ->0->null
            # node next nya adalah 0
            # node next data sebelemunya (9) adalah data baru yang kita masukan
            # 2->4->9->9->7->0->null


# Deklarasikan function insert_list dengan parameter data_list
    def insert_list(self, data_list):
        # Iterasi data_list ke data, ambil tiap2 data_list, masukan ke node terakhir dari list
        for data in data_list:
            # Masukan nilai menggunakan funtion insert_at_end
            self.insert_at_end(data)
            
# Cara Reverse Linked List
    def print_reverse(self):
        # Dapatkan Nilai head didalam node, dan masukan ke Variable EndNode
        EndNode = self.head
        # Selama EndNode.next tidak kosong, maka update ke next berikutnya sampai mencapai tail
        while(EndNode.next is not None):
            EndNode = EndNode.next
        # Jika EndNode.next kosong, maka kita telah mecapai akhir dari LinkedList
        GetEnd = EndNode
        
        # Buat Variable Untuk menampung String
        str_1 = ""
        # Selama GetEnd Tidak None, maka kita update ke prev, untuk mendapatkan nilai kebalikannya
        while(GetEnd is not None):
        # masukan tiap2 nilai yang didapat kedalam String
            str_1 += str(GetEnd.data) + "-->"
        # Update GetEnd ke GetEnd.prev
            GetEnd = GetEnd.prev
        # Print seluruh elemen yang didapat
        print(str_1)
        
# Remove From The Begining
    def remove_at_begining(self):
        if self.head is None:
            print("Linked List Kosong")
        self.head = self.head.next

        # 2->4->9->9->0->null
        # Remove from the begining
        # Result
        # 4->9->9->0->null
        
# Remove From The last
    def remove_at_the_end(self):
        # Jika self head itu none
        if self.head is None:
            # Maka print Linked list ksong
            print("Linked List Kosong")
        # Tetap kan itr ke self.head
        itr = self.head
        # Selama itr next next memliki value, maka update itr, untuk mengambil data 2 terakhir di linked list
        while(itr.next.next is not None):
            # Update ITR
            itr = itr.next
        # data 2 terakhir dari linkedlist dijadikan null
        itr.next = None 

        # 2->4->9->9->0->null
        # Remove at the end
        # Result
        # 2->4->9->9->null
        
        
        


# Remove From Certain Point
# Buat Fungsi Untuk Menghapus Value dari index tertentu
    def remove_at(self, index):
        # Cek jika index kurang dari atau lebih dari panjang linked list, maka index yang dimasukan invalid
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid")
        
        # Jika index sama dengan nol maka, head ditetapkan ke nilai next dari head yang skrg
        if index == 0:
            self.head = self.head.next

        # Buat count sama dengan nol
        count = 0
        # Buat itr sama dengan head
        itr = self.head
        # Selama itr memiliki value
        while(itr):
            # Cek jika count sama dengan index - 1
            if count == index -1:
                # Maka tetapkan itr next ke itr next next agar value yang ada di antara dua index terhapus
                itr.next = itr.next.next
                # Jika sudah terhapus maka break
                break
            # Update itr ke next
            itr.next
            # Update count ++
            count+=1

# Menghitung panjang linkedlist
    def get_length(self):
    # Inisialisasi 0 pada count
        count = 0
        # Inisialisasi self.head pada variable baru
        itr = self.head
        # Selama itr ada value
        while(itr):
            # Update itr ke itr.next
            itr = itr.next
            # Hitung count
            count+=1
        # Jika itr mencapai tail, maka return nilai panjang linked list
        return count
    
    def reverse(self):
        # Untuk menyimpan Current Data
        curr = self.head
        # Kosong kan Prev
        prev = None
        
        # Selama Current Not null, Berarti curr belum mencapai tail
        while(curr is not None):
            # tetapkan next ke currenct next
            # None -> 1 -> 2 -> 3
            # curr = 1 dan curr.next = 2
            next = curr.next
            # tetapkan current next ke prev
            # # None -> 1 -> 2 -> 3
            # menjadi None <- 1 -> 2 -> 3
            # karena prev = None dan currnext
            curr.next = prev
            # tetapkan prev ke curr
            # # None <- 1 -> 2 -> 3
            # prev menjadi 1
            prev = curr
            # dan curr menjadi 2
            curr = next
        # Jika curr None, maka tetapkan head ke prev
        self.head = prev
        


        
        



list = List()
list_3 = Node('3')
list_2 = Node('2', list_3)
list.head = Node('1', list_2)
# list_3.prev = list_2
# list_2.prev = list.head


list.insert_at_begining('0')
# list.insert_at_begining('0')

list.insert_list(['4', '5'])

list.printval()
list.reverse()
list.printval()

# panjang = list.get_length()
# print(panjang)
# list.remove_at(1)
# list.insert_at(1, "7")
# list.remove_at_the_end()
# list.printval()



