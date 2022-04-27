import queue
import pwinput
import os

akun = {"username": [ "rizq", "fathul","marliani"],
        "password": [ "1", "2","3"]}

admin1 = {"username": ["admin"],
        "password": ["1"]}

baju = {"nama" : ["kaos","kemeja"],
        "harga" : [100000,200000]}

nama_user = []

# Memasukkan username ke variable nama_user
for i in akun["username"]:
    nama_user.append(i)

# Class Node
class Node: # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign 
        self.next = None # Initialize next as null
        self.prev = None # Initialize prev as null

# Stack class contains a Node object
class Stack:
    # Function to initialize head
    def __init__(self):
        self.head = None

# Function to add an element data in the stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

# Function to pop top element and return the element from the stack
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp 

# Function to return top element in the stack
    def top(self):
        return self.head.data

        # Function to return the size of the stack
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

        # Function to check if the stack is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Function to print the stack
    def printstack(self):
        print("stack elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end ="->")
            temp = temp.next

stack = Stack()

# QUICK SORT
def partition(arr, low, high):
	i = (low-1)		 
	pivot = arr[high]	 
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

# Fibonaci search
def searching(isi, x, n):
    fibonaci2 = 0 
    fibonaci1 = 1 
    fibonaci = fibonaci2 + fibonaci1 
    while (fibonaci < n):
        fibonaci2 = fibonaci1
        fibonaci1 = fibonaci
        fibonaci = fibonaci2 + fibonaci1
    offset = -1
    while (fibonaci > 1):
        i = min(offset+fibonaci2, n-1)
        if (isi[i] < x):
            fibonaci = fibonaci1
            fibonaci1 = fibonaci2
            fibonaci2 = fibonaci - fibonaci1
            offset = i
        elif (isi[i] > x):
            fibonaci = fibonaci2
            fibonaci1 = fibonaci1 - fibonaci2
            fibonaci2 = fibonaci - fibonaci1
        else:
            return i
    if(fibonaci1 and isi[n-1] == x):
        return n-1
    return -1

# Mencari nama user
def search():
    n = len(nama_user)
    x = input("Masukan Yang ingin anda cari : ")
    isi = searching(nama_user, x, n)
    if isi >= 0:
        print("Ditemukan di index ke :",isi)
        t = input("Enter ...")
    else:
        print(x,"Nama Tidak ada di list")
        t = input("Enter ...")

# Mencari Nama Baju
def search_baju():
    n = len(baju.get("nama"))
    x = input("Masukan Yang ingin anda cari : ")
    isi = searching(baju.get("nama"), x, n)
    if isi >= 0:
        print("Ditemukan di index ke :",isi)
        t = input("Enter ...")
    else:
        print(x,"Nama Tidak ada di list")
        t = input("Enter ...")

# Fungsi untuk membuat angka menjadi format Rupiah
def rp(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return rp(q) + '.' + p

# Melihat data baju
def lihat():    
    print("=====================")
    print("1. Lihat Data")
    print("2. Lihat Jumlah Data")
    print("=====================")
    pilih = input("Pilih : ")
    if pilih == "1":
        if len(baju.get("nama"))<1 :
            print("Data Masih Kosong")
            t = input("Enter Untuk Melanjutkan...")
        else:
            print("--- MRF STORE ---")
            nb = baju.get("nama")
            hb = baju.get("harga")
            for i in range(len(baju.get("nama"))):
                print(f"--> {nb[i]}\t\t{rp(hb[i])}")            
            print("\n")
            t = input("Enter Untuk Melanjutkan...")    
    if pilih == "2":
        pass
        a = baju.get("nama")        
        for i in range(len(a)):
            s = a[i]
            stack.push(s)
        print("Jumlah Data :",stack.size()) 
        stack.printstack()
        t = input("Enter Untuk Melanjutkan...")            
        for i in range(len(a)):
            stack.pop()            

# Belanja
def belanja():    
    try :
        if len(baju.get("nama"))<1 :
            print("Data Masih Kosong")
            t = input("Enter Untuk Melanjutkan...")  
        else:
            os.system('cls')
            print("|=============================|")
            print("|         MRF STORE           |")
            print("|=============================|")    
            nb = baju.get("nama")
            hb = baju.get("harga")
            for i in range(len(baju.get("nama"))):
                print(f"-->  {nb[i]}\t\t{rp(hb[i])}")            
            print("\n")
            beli = input("Pilih sesuai Nama diatas : ")
            idx = baju.get("nama").index(beli)
            # jumlah_harga = baju["harga"][idx]
            print(f"Anda Membeli {nb[idx]} Harga = {rp(hb[idx])}")
            print("\n")
            print("Terima Kasih Telah Berbelanja")
            del baju["nama"][idx]
            del baju["harga"][idx]
            t = input("Enter Untuk Melanjutkan...")
    except:
        print("Masukkan Sesuai nama baju yang ingin di beli")
        t = input("Enter Untuk Melanjutkan...")

# Menambah Data Baju
def tambah():
    nama = input('Masukan Nama Baju : ')  
    while True:
        harga = int(input('Masukan Harga baju : '))            
        if harga < 1000:
            print("Angka Tidak Boleh kurang dari 1000")
        else:
            break                         
    baju.get("nama").append(nama)
    baju.get("harga").append(harga)
    print("Berhasil Menambahkan")
    t = input("Enter ...")

# Menghapus Data Baju
def hapus():  
    try:
        if len(baju.get("nama"))<1 :
            print("Data Masih Kosong")
            t = input("Enter Untuk Melanjutkan...")  
        else:
            print("--- MRF STORE ---")
            nb = baju.get("nama")
            hb = baju.get("harga")
            for i in range(len(baju.get("nama"))):
                print(f"--> {nb[i]}\t\t{rp(hb[i])}")            
            print("\n")
            t = input("Enter Untuk Melanjutkan...")  
            nama = (input("Masukkan Nama baju yang ingin dihapus : "))
            idx = baju.get("nama").index(nama)    
            del baju["nama"][idx]
            del baju["harga"][idx]
            print("Barang berhasil dihapus")
            t = input("Enter ...")
    except:
        print("Masukkan nama baju yang ingin dihapus")
        t = input("Enter ...")

# Mengubah Data Baju
def ubah():
    try:
        if len(baju.get("nama"))<1 :
            print("Data Masih Kosong")
            t = input("Enter Untuk Melanjutkan...")  
        else:
            print("--- MRF STORE ---")
            nb = baju.get("nama")
            hb = baju.get("harga")
            for i in range(len(baju.get("nama"))):
                print(f"--> {nb[i]}\t\t{rp(hb[i])}")            
            print("\n")
            t = input("Enter Untuk Melanjutkan...")  
            nama = (input("Masukkan Nama baju yang ingin diubah : "))
            idx = baju.get("nama").index(nama)    
            del baju["nama"][idx]
            del baju["harga"][idx]
            nama = input('Masukan Nama Baju : ')  
            while True:
                harga = int(input('Masukan Harga baju : '))            
                if harga < 1000:
                    print("Angka Tidak Boleh kurang dari 1000")
                else:
                    break                         
            baju.get("nama").append(nama)
            baju.get("harga").append(harga)
            print("Barang berhasil diubah")
            t = input("Enter ...")
    except:
        print("Masukkan nama baju yang ingin diubah")
        t = input("Enter ...")

# Menu Login
def menu1():
    print("|=============================|")
    print("|            MENU             |")
    print("|=============================|")
    print("|   1. Login User             |")
    print("|   2. Login Admin            |")
    print("|   3. Register (Pelanggan)   |")
    print("|   4. Keluar                 |")
    print("|=============================|")
    
# Login User    
def loguser():
    try:
        username = input("masukkan Username : ")
        password = pwinput.pwinput("Masukkan Password : ")
        daftar = akun.get("username").index(username)
        if username == akun.get("username")[daftar] and password == akun.get("password")[daftar]:
            print("Berhasil Login")
            menu_user()
        else : 
            print("Gagal Login")
            t = input("Enter untuk Kembali...")
    except ValueError:
            print("Maaf Username yang anda masukkan tidak tersedia")
            t = input("Enter untuk Kembali...")

# Login Admin
def logadmin():
    try:
        username = input("masukkan Username : ")
        password = pwinput.pwinput("Masukkan Password : ")
        daftar = admin1.get("username").index(username)
        if username == admin1.get("username")[daftar] and password == admin1.get("password")[daftar]:
            print("Welcome admin")
            menu_admin()
        else : 
            print("Gagal Login")            
            t = input("Enter untuk Kembali...")
    except ValueError:
            print("Maaf Username yang anda masukkan tidak tersedia")
            t = input("Enter untuk Kembali...")

# Daftar User
def register_user():
    while True:
        us = input("Masukkan username : ")
        if len(us) < 1:
            print("Minimal Nama 2 Kata")
            return False
        if us in akun.get("username"):
            print("Username anda telah terdaftar")
        else:
            pw = input("Masukkan Password : ")
            akun.get("username").append(us)
            akun.get("password").append(pw)
            nama_user.append(us)
            break
    print("Berhasil Register")
    t = input("Enter untuk Kembali...")

def menu_user():
    while True:
        os.system('cls')
        print("|=============================|")
        print("|         MENU(USER)          |")
        print("|=============================|")
        print("|   1. Lihat Baju             |")
        print("|   2. Belanja                |")
        print("|   3. Cari Baju              |")
        print("|   4. Kembali                |")
        print("|   5. Keluar                 |")
        print("|=============================|")
        pilih = (input("Pilih : "))
        if pilih == "1":
            lihat()
        elif pilih == "2":
            belanja()
        elif pilih =="3":
            search_baju()
        elif pilih == "4":
            kembali()
        elif pilih == "5":
            exit()
        else:
            print("Pilih Sesuai Angka DI Menu")
            t = input("Enter untuk Kembali...")

def menu_admin():
    while True:
        os.system('cls')
        print("|=============================|")
        print("|         MENU(ADMIN)         |")
        print("|=============================|")
        print("|   1. Masukan Barang Baru    |")
        print("|   2. Lihat Barang           |")
        print("|   3. Hapus Barang           |")
        print("|   4. Ubah Barang            |")
        print("|   5. Lihat User             |")
        print("|   6. Cari User              |")
        print("|   7. Kembali                |")
        print("|   8. Keluar                 |")
        print("|=============================|")
        pilih = (input("Pilih : "))
        if pilih == "1":
            tambah()
        elif pilih == "2":
            lihat()
        elif pilih == "3":
            hapus()
        elif pilih == "4":
            ubah()
        elif pilih == "5":
            print("="*36)
            print("1. Lihat Data User Secara ASC (A-Z)")
            print("2. Lihat Data User Secara DESC (Z-A)")
            print("="*36)            
            pilihan = input ("Pilih Menu : ")
            if pilihan == "1":
                print("Data User")
                n = len(nama_user)
                quickSort(nama_user, 0, n-1)
                no =1
                for x in nama_user:
                    print(f"{no}. {x}")
                    no +=1
                print("="*20)
                t = input("Enter ...")

            elif pilihan == "2":
                print("Data User")
                n = len(nama_user)
                quickSort(nama_user, 0, n-1 )
                idx = -1                    
                no = 1
                for i in range(0, len(nama_user)) :                                        
                    print(f"{no}. {nama_user[idx]}") 
                    idx -= 1                          
                    no += 1 
                print("="*20)
                t = input("Enter ...")
            
            else:
                print("Pilih Sesuai Angka Diatas")                          
                t = input("Enter untuk Kembali...")
        elif pilih == "6":
            search()
        elif pilih == "7":
            kembali()
        elif pilih == "8":
            exit()

# Kembali ke menu
def kembali_admin():
    print("\n")
    input("Tekan Enter untuk kembali ke Menu...")
    menu_admin()
def kembali_user():
    print("\n")
    input("Tekan Enter untuk kembali Ke Menu...")
    menu_user()
def kembali():
    print("\n")
    input("Tekan Enter untuk kembali Ke Menu...")
    menu_login()

def menu_login():
    os.system('cls')
    while True:
        menu1()
        pilih = (input("Pilih : "))
        if pilih == "1":
            loguser()            
        elif pilih == "2":
            logadmin()            
        elif pilih == "3":
            register_user()
        elif pilih == "4":
            exit()
        else :print("Pilihan Tidak Tersedia")

menu_login()
