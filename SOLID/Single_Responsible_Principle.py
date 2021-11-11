# Class harus hanya ada satu alasan untuk dirubah
# Satu Class harus memunyai function yang spesifik
# jika kelas memiliki lebih dari satu tugas, ini akan tergabung-gabung
# Pengubahan satu tugas menghasilkan modifikasi/pengaruh ke tugas lainnya

class Employee:
    def __init__(self, nama, task):
        self.__nama = nama
        self.__task = task

    def get_name(self):
        return self.__nama

    def get_task(self):
        return self.__task

class reportJob():
    def printJobReport(self, user) -> Employee:
        return user.get_name(), user.get_task()



user_1 = Employee("Taufiiqul Hakim", "Programming")
user_2 = Employee("Taufiiqul Hakim 2", "Anotated")

user_1_report = reportJob()
user_2_report = reportJob()
print(user_1_report.printJobReport(user_1))
print(user_2_report.printJobReport(user_2))
