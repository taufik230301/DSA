from KaryawanFactory import KaryawanFactory

manager_1 = KaryawanFactory.createManager('Taufik')

staff_1 = KaryawanFactory.crateStaff('Kresna')
print(manager_1.getNama())
print(staff_1.getNama())