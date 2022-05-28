# Project Akhir Toko Roti

import csv
import pwinput
from prettytable import PrettyTable
from pyfiglet import figlet_format
csv_filename = "E:\Bahasa Pemrograman\Latihan\Sch\PA\struk.csv"
tabel = PrettyTable()

nama_akun = []
list_harga = []
total_harga = []
list_barang = []
list_jumlah_barang = []

# Daftar Akun Username dan Password Yang Tersedia
akun = {"username": ["admin", "user", "rizq"],
        "password": ["1", "123", "1"]
        }

# Daftar Menu Yang Tersedia
menu = {"No": [1, 2, 3, 4, 5, 6, 7],
        "Barang": ["Roti Coklat", "Roti Strawberry", "Roti Green Tea", "Roti Durian", "Roti Keju", "Roti Tiramisu", "Roti Vanila", ],
        "Harga": [12000, 15000, 14000, 10000, 11000, 14000, 12000],
        }

# Membuat Judul Pada Feild Table
tabel.field_names = ["No", "Barang", "Harga"]

# Fungsi untuk membuat angka menjadi format Rupiah
def rp(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return rp(q) + '.' + p

# Fungsi Untuk Mendaftar Username dan Password Baru


def register_user():
    while True:
        us = input("Masukkan username : ")
        if us in akun.get("username"):
            print("Username anda telah terdaftar")
        else:
            pw = input("Masukkan Password : ")
            akun.get("username").append(us)
            akun.get("password").append(pw)
            break
    print("Berhasil Register")


# Fungsi Untuk Memasukkan Data Barang ke dalam tabel
def tambahkan():
    while True:
        Nomor = menu["No"][-1]
        no = Nomor + 1
        br = input("Nama Barang : ")
        hg = int(input("Masukkan Harga : "))
        if br in menu.get("Barang"):
            print("Barang Sudah Ada")
        else:
            if hg < 1000:
                print("Angka Tidak Boleh kurang dari 1000")
            else:
                menu.get("No").append(no)
                menu.get("Barang").append(br)
                menu.get("Harga").append(hg)
                print("Berhasil menambah barang")
                break

# Fungsi Untuk Mengubah Nama dan Harga Barang


def ubah():
    print(tabel)
    n = int(input("masukkan nomor barang yang mau diubah : "))
    brg = input("Masukkan Nama Barang baru : ")
    while True:
        hg = int(input("Masukkan Harga baru : "))
        if hg < 1000:
            print("Angka Tidak Boleh kurang dari 1000")
        else:
            break
    indexnya = menu.get("No").index(n)
    menu.get("Barang")[indexnya] = brg
    menu.get("Harga")[indexnya] = hg
    print("Berhasil mengubah barang")

# Fungsi Untuk Menghapus list_barang yang berada dalam daftar tabel


def hapus():
    print(tabel)
    nobarang = int(input("Masukkan No barang yang ingin dihapus : "))
    t = menu.get("No").index(nobarang)
    del menu["No"][t]
    del menu["Barang"][t]
    del menu["Harga"][t]
    ind = 0
    for i in range(len(menu.get("No"))):
        ind += 1
        menu.get("No")[i] = ind
    print("Barang berhasil dihapus")

# Fungsi Untuk Memasukkan dictionary Kedalam Tabel


def btabel():
    tabel.clear_rows()
    for i in range(len(menu.get("No"))):
        tabel.add_row([menu.get("No")[i], menu.get("Barang")[i],rp(menu.get("Harga")[i])])

# Menu Login


def menu1():
    print(f"""
    ==================================================
    |                  TOKO ROTI                     |
    ==================================================
    |                {"[1] Login"}                      |   
    |                {"[2] Buat Akun"}                  |   
    ==================================================""")

# Menu Admin


def menu2():
    print(f"""
    ==================================================
    |                    Menu                        |
    ==================================================
    |               {"[1] Tambahkan barang"}             |   
    |               {"[2] Tampilkan barang"}             |   
    |               {"[3] Ubah barang"}                  |   
    |               {"[4] Hapus barang"}                 |   
    |               {"[5] Lihat Riwayat Pembelian"}      |   
    |               {"[6] Keluar"}                       |   
    ==================================================""")

# Menu User


def menu3():
    print(f"""
    ==================================================
    |                    Menu                        |
    ==================================================
    |               {"[1] Belanja"}                      |   
    |               {"[2] Keluar"}                       |   
    ==================================================""")

# Program Transaksi


def transaksi():
    btabel()
    while True:
        try:
            print(tabel)
            beli = int(input("Pilih sesuai No diatas : "))
            beli2 = menu.get("No").index(beli)
            jumlah_barang = int(input("Jumlah Barang yang ingin di beli : "))
            barangnya = menu["Barang"][beli2]
            jumlah_harga = jumlah_barang * menu["Harga"][beli2]
            total_harga.append(jumlah_harga)
            list_barang.append(barangnya)
            list_jumlah_barang.append(jumlah_barang)
            list_harga.append(jumlah_harga)
            break
        except ValueError:
            print("Angka tidak sesuai")

# Fungsi Melihat Pembelian


def lihat_pembelian():
    isi = []
# buka file CSV dengan mode R / Baca
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            isi.append(row)
    row_count = sum(1 for row in isi)
    print(isi)
    print("-" * 55)
    print("\t\tDaftar Riwayat Pembelian")
    print("-" * 55)
    print("Nama \t   Belanja \t\t Harga")
    print("-" * 55)

    harga = []
    # Looping untuk mengeluarkan datanya
    for data in isi:
        print(f"{data['nama_user']} \t {data['belanja']}     \t{rp(data['harga'])}")
        harga.append(int(data['harga']))
    tharga = sum(harga)
    print("-" * 55)
    print(f"Total Data : {row_count} \t \t\t{rp(tharga)}")
    print("-" * 55)

# Fungsi Menambah Barang ke Struk.csv
def simpan_struk():
    with open(csv_filename, mode='a', newline='') as csv_file:
        fieldnames = ['nama_user', 'belanja', 'harga']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for i in range(len(list_barang)):
            nama_user = nama_akun[0]
            belanja = f"{list_jumlah_barang[i]} {list_barang[i]}"
            harga = list_harga[i]
            writer.writerow(
                {'nama_user': nama_user, 'belanja': belanja, 'harga': harga})

# Program struk belanja
def struk():
    hasil = sum(total_harga)

    print("\n----------------------------------")
    print("\t      Toko Roti")
    print("----------------------------------")
    for i in range(len(list_barang)):
        print(
            f"{list_jumlah_barang[i]} {list_barang[i]}     \t{rp(list_harga[i])}")
    print("----------------------------------")
    print(f"Total\t\t\t{rp(hasil)}")
    print("----------------------------------")


def admin():
    while True:
        try:
            menu2()
            btabel()
            pilih = int(input("Pilih : "))
            if pilih == 1:
                tambahkan()
                kembali_admin()
            elif pilih == 2:
                print(tabel)
                kembali_admin()
            elif pilih == 3:
                ubah()
                kembali_admin()
            elif pilih == 4:
                hapus()
                kembali_admin()
            elif pilih == 5:
                lihat_pembelian()
                kembali_admin()
            elif pilih == 6:
                exit()
            else:
                print("Angka Yang anda masukkan salah\nSilahkan Coba Lagi")
        except ValueError:
            print("Masukkan sesuai angka di menu")


def user():
    menu3()
    try:
        pilih = int(input("Pilih : "))
        if pilih == 1:
            while True:
                transaksi()
                pilih = input("Ada Lagi Yang ingin dibeli [y/t] : ")
                if pilih == "y":
                    continue
                elif pilih == "t":
                    while True:
                        struk()
                        pilih = input("Apakah anda ingin keluar [y/t] : ")
                        if pilih == "t":
                            kembali_user()
                        elif pilih == "y":
                            print("Terima Kasih Telah berbelanja")
                            simpan_struk()
                            exit()
        elif pilih == 2:
            exit()
        else:
            print("Pilih Sesuai Angka di atas")
    except ValueError:
        print("Pilih Sesuai Angka diatas")


def kembali_admin():
    print("\n")
    input("Tekan Enter untuk kembali ke Menu...")
    admin()


def kembali_user():
    print("\n")
    input("Tekan Enter untuk kembali Ke Menu...")
    user()


# Program Menu Utama
while True:
    try:
        # Program Login
        menu1()
        pilih = int(input("Pilih : "))
        try:
            if pilih == 1:
                username = input("masukkan Username : ")
                password = pwinput.pwinput("Masukkan Password : ")
                daftar = akun.get("username").index(username)
                if username == akun.get("username")[0] and password == akun.get("password")[0]:
                    print("Login berhasil")
                    print(figlet_format("Welcome Admin", font="standard"))
                    admin()

                # Login User
                elif username == akun.get("username")[daftar] and password == akun.get("password")[daftar]:
                    print(
                        "login berhasil\n---------------------Selamat Datang---------------------")
                    nama_akun.append(username)
                    print(figlet_format("TOKO ROTI", font="standard"))
                    user()
                else:
                    print("Maaf Password anda salah")

            # Register User
            elif pilih == 2:
                register_user()
            else:
                print("Angka yang anda masukkan tidak terdaftar")

        except ValueError:
            print("Maaf Username yang anda masukkan tidak tersedia")
    except ValueError:
        print("Angka tidak sesuai")