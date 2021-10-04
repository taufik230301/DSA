class Circular_Queue:
    def __init__(self, k):
        # Buat Object Costruct 
        self.k = k
        self.queue = [None]*5
        self.head = -1
        self.tail = -1

    # Buat fungsi untuk memasukan nilai kedalam circular queue, data merupakan parameter untuk nilai baru
    def enqueue(self, data):
        # Jika tail ditamah satu dan di modulo panjang queue sama dengan head, artinya queue penuh
        # Karena tail sudah samapai batas masimum index didalam queue dan head sudah menjadi 0
        if ((self.tail +1 ) % self.k == self.head):
            print("Queue Penuh")
            # Jika head -1 maka
        elif (self.head == -1):
            # Update head dan tail ke 0
            self.head = 0
            self.tail = 0
            # Masukan data baru ke index 0
            self.queue[self.tail] = data
        else:
            # masukan nilai tail ditambah 1 dan di modulo panjang queue ke dalam tail
            self.tail = (self.tail + 1 )% self.k
            # dan masukan data ke dalam queue berdasarkan index tail 
            self.queue[self.tail] = data
    
    # Fungsi untuk mencetak queue
    def print_queue(self):
        # Cek jika head sama dengan -1
        if (self.head == -1):
            print("TIdak ada lement didalam Queue")
        # Jika tail lebih dari sama dengan head
        elif (self.tail>= self.head):
            # Maka cetak seluruh elemt mulai dari head = 0 sampai tail +1
            for i in range(self.head, self.tail +1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")

queue_1 = Circular_Queue(5)

queue_1.enqueue(1)

queue_1.print_queue()



        