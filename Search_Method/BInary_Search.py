# Python3 Program for recursive binary search.

def binarySearch (arr, awal, akhir, x):
	# Cek apakah panjang elemnt array lebih dari low
	if akhir >= awal:

	# mencari mid, panjang array + awal array // 2 
		mid = akhir+awal // 2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binarySearch(arr, awal, mid-1, x)

		else:
			return binarySearch(arr, mid + 1, akhir, x)

	else:
	
		return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 3


result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element Ada Didalam Array, di Index ke - % d" % result)
else:
	print ("Element Tidak ada Dialam Array")
