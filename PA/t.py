from random import randint

def merge_sort(lst, order = 'asc'): #fungsi untuk mengurutkan list
  if len(lst) <= 1: #panjang list kurang dari atau sama dengan 1
    return lst #jika list kurang dari atau sama dengan 1, maka return list

  mid = len(lst) // 2  #membelah list menjadi 2 bagian, bagian kiri dan kanan

  left = merge_sort(lst[0:mid], order) #membelah bagian kiri
  right = merge_sort(lst[mid:len(lst)], order) #membelah bagian kanan
  
  return merge(left, right, order) # TEST CASES


def merge(left, right, order): #fungsi untuk menggabungkan 2 list
  result = [] #membuat list kosong
  i, j = 0, 0 #membuat index kosong

  while i < len(left) and j < len(right): #mengecek apakah index kiri dan kanan masih ada

    # mengecek apakah salah satu left atau right ada yang isalpha atau alphabet
    if str(left[i]).isalpha() or str(right[j]).isalpha() :
      compare = str(left[i]) < str(right[j]) if order is 'asc' else str(left[i]) > str(right[j])
    else :
      compare = int(left[i]) < int(right[j]) if order is 'asc' else int(left[i]) > int(right[j])

    if compare : #jika index kiri lebih kecil dari index kanan
      result.append(left[i]) #maka append index kiri ke list kosong
      i += 1 #index kiri bertambah 1
    else: #jika index kanan lebih kecil dari index kiri
      result.append(right[j]) #maka append index kanan ke list kosong
      j += 1 #index kanan bertambah 1

  result += left[i:] #mengecek apakah index kiri masih ada atau tidak
  result += right[j:] #mengecek apakah index kanan masih ada atau tidak

  return result #mengembalikan list yang sudah diurutkan

# Mengubah int kalau dia isnumeric()
# "abc" != isnumeric, "123" == isnumeric
def numeric_str_ubah_ke_int(nilai) :
  return int(nilai) if str(nilai).isnumeric() else nilai

# Fungsi untuk meratakan list
def ratakan_list(list_yang_mau_diratakan) :
  list_rata = []

  for lymd in list_yang_mau_diratakan :
    if type(lymd) == list :

      # kalau tipe nilainya == list, maka tambahkan semua nilainya ke dalam list_rata
      list_rata += [numeric_str_ubah_ke_int(nilai) for nilai in lymd]

    elif type(lymd) == dict :

      # kalau tipe nilainya == dict, maka ambil dulu keys sama values nya terpisah, lalu diubah ke int dan ditambahkan ke list_rata
      keys = [numeric_str_ubah_ke_int(nilai) for nilai in lymd.keys()]
      values = [numeric_str_ubah_ke_int(nilai) for nilai in lymd.values()]
      list_rata += [*keys, *values]
      
    elif type(lymd) == str :

      # kalau tipe nilainya == string, cek dulu dia isnumeric atau tidak, lalu tambahkan ke list_rata
      list_rata.append(int(lymd) if lymd.isnumeric() else lymd)

    else :
      # kalau tipenya == int yaudah langsung tambah aja
      list_rata.append(lymd)

  return list_rata

soal_nomor_1 = [[2, 3, "4"], 2, 4, 97, {"a": "sd", "b": "c", 3:5}, 1, 3, "aduh", 1, 223]
jawaban_nomor_1 = merge_sort(ratakan_list(soal_nomor_1))

soal_nomor_2 = [32, 48, 7, 45, 50, 4, 23, 44, 21, 28] # [randint(0, 50) for i in range(10)]
jawaban_nomor_2 = merge_sort(soal_nomor_2, 'desc')

print(f"""
  1. Diketahui terdapat sebuah data list seperti gambar diatas, dari data tersebut maka :
    a. Buatlah program sorting yang dapat mengurutkan nilai dari yang terkecil hingga yang terbesar.
    b. Algoritma sorting yang digunakan adalah Merge Sort / Quick Sort / Shell Sort (pilih salah satu)

    Jawab :
    Sebelum : {soal_nomor_1}
    Sesudah : {jawaban_nomor_1}
    Algoritma yang dipakai adalah merge sort.

  2. Dari hasil output yang telah kalian dapatkan tadi, maka :
    a. Buatlah program sorting yang dapat mengurutkan nilai dari yang terbesar hingga yang
    terkecil.
    b. Algoritma sorting yang digunakan adalah Merge Sort / Quick Sort / Shell Sort (pilih salah
    satu)
    c. Gambarkanlah Visualisasi datanya (seperti yang terdapat pada modul).

    Jawab :
    Sebelum : {soal_nomor_2}
    Sesudah : {jawaban_nomor_2}
    Algoritma yang dipakai adalah merge sort.
""")