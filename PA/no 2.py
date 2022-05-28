from random import randint

mylist = [randint(0,50)for i in range(10)]
print("------- Sorting Menggunakan Shell Sort -------")
print(f"Array = {mylist}")

def shellSort(array, n):
    interval = n // 2
    while interval > 0:        
        for i in range(interval, n):
            temp = array[i]           
            j = i            
            while j >= interval and array[j - interval] < temp:                
                array[j] = array[j - interval]                
                j -= interval
            array[j] = temp
        print(f"GAP = {interval}")
        interval //= 2
        print(array)
        print("\n")

size = len(mylist)
shellSort(mylist, size)
print('Mengurutkan Dari Terbesar ke Terkecil')
print(mylist)