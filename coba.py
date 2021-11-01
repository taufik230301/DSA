list_1 = "LISTSIL"

mid = len(list_1)//2

i = 0

while(i <= mid):
    # Jika index awal, dan index akhir dari sebuah list sama, maka lanjutkan iterasi.
    if list_1[i] == list_1[-i-1]:  
        pass
    # Jika index awal. dan index akhir dari sebuah list tidak sama, maka print bukan polindrom
    elif list_1[i] != list_1[-i-1]:
        print("Bukan Polindrom")
        # Berhenti program
        break
    # Jika i sama dengan mid, artinya pengecekan sudah selesai, karena tidak ada kendala pada kondisi pertama
    # Maka print polindrom
    if i == mid:
        print("Polindrom")
    i+=1


    
    



