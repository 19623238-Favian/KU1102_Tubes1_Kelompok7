# Kelompok 7 / Program Sistem Pemesanan Makanan dan Minuman
# Anggota:
# 1. Shannon Aurellius Anastasya Lie / 19623105
# 2. Nawaf Amjad Rizqi Aldaha Ismail / 19623217
# 3. Favian Rafi Laftiyanto / 19623238
# 4. Muhammad Riyan Rajab / 19623259
# 5. Ni Made Sekar Jelita Parameswari / 19623308

# KAMUS
# nomor_pesanan, sum_pendapatan, total_harga, jumlah_porsi, total_makan, total_harga, makanan_dipesan, minuman_dipesan, pesan_makanan, pesan_minuman, jumlah_gelas, metode_pembayaran, uang_tunai : int
# pesanan, program_makan, program_minum : bool
# pertanyaan_makan, pertanyaan_minum, stop_makan, stop_minum, jeda, stop_pesanan : str
# menu_makanan, menu_minuman : array[0..10] of str
# harga_makanan, harga_minuman, stok_makanan, stok_minuman : arra[0..10] of int
# daftar_pembelian : array[0..len(menu_makanan + menu_minuman)] of str and int

# ALGORITMA
pesanan = True # Boolean untuk persyaratan while loop berjalannya program
nomor_pesanan = 1 # Variabel nomor pesanan
sum_pendapatan = 0 # Variabel Total Pendapatan
total_harga = 0 # Variabel total tagihan makan

# Array menyimpan data nama makanan, harga, dan stok makanan
menu_makanan = ["Soft Cookies", "Croissant", "Cheese Shortcake", "Tiramisu Cake", "Kue Pancong", "Fried Banana", "Spaghetti", "Fettuccine", "Panna Cotta", "Choux Pastry"]
harga_makanan = [15_000, 19_000, 23_000, 28_000, 10_000, 18_000, 33_000, 30_000, 28_000, 16_000]
stok_makanan = [30 for i in range(len(menu_makanan))]

# Array menyimpan data nama minuman, harga, dan stok minuman
menu_minuman = ["Americano", "Cappuccino", "Caffe Latte","Caffe Macchiato","Hot Chocolate","Chamomile Tea", "Earl Grey Tea", "Green Tea", "Tipsy Ice", "Sweet Iced Tea"]
harga_minuman = [18_000, 23_000, 25_000, 22_000, 30_000, 24_000, 21_000, 28_000, 25_000, 10_000]
stok_minuman = [30 for i in range(len(menu_minuman))]

# Function/Prosedur untuk pemesanan makanan
def pesan_makan(pesan_makanan, jumlah_porsi):
    if (jumlah_porsi > stok_makanan[pesan_makanan-1]):
        print("Menu tersebut sudah habis. Silakan pesan menu lainnya.")
        return
    else:
        total_makan = jumlah_porsi * harga_makanan[pesan_makanan-1]
        print(f"  ↪ {menu_makanan[pesan_makanan-1]} {jumlah_porsi} Porsi : Rp {total_makan}.")
        stok_makanan[pesan_makanan-1] -= jumlah_porsi
        daftar_pembelian[pesan_makanan-1] = menu_makanan[pesan_makanan-1], jumlah_porsi, total_makan
        return [stok_makanan[pesan_makanan-1], daftar_pembelian[pesan_makanan-1], total_makan, total_harga]
    
# Function/Prosedur untuk pemesanan minuman
def pesan_minum(pesan_minuman, jumlah_gelas):
    if (jumlah_gelas > stok_minuman[pesan_minuman-1]):
        print("Menu tersebut sudah habis. Silakan pesan menu lainnya.")
        return
    else:
        total_makan = jumlah_gelas * harga_minuman[pesan_minuman-1]
        print(f"  ↪ {menu_minuman[pesan_minuman-1]} {jumlah_gelas} Gelas : Rp {total_makan}.")
        stok_minuman[pesan_minuman-1] -= jumlah_gelas
        daftar_pembelian[pesan_minuman+9] = menu_minuman[pesan_minuman-1], jumlah_gelas, total_makan
        return [stok_minuman[pesan_minuman-1], daftar_pembelian[pesan_minuman+9], total_makan]

# Prosedur untuk mencetak makanan yang telah dipesan pada bill
def bill_makan(menu_nomor):
    if daftar_pembelian[menu_nomor] != 0:
        print(f"\t\t\t\t\t\t| {daftar_pembelian[menu_nomor][0]}     \t{daftar_pembelian[menu_nomor][1]} Porsi  :   Rp {daftar_pembelian[menu_nomor][2]}\t    |")
        return

# Prosedur untuk mencetak minuman yang telah dipesan pada bill
def bill_minum(menu_nomor):
    if daftar_pembelian[menu_nomor] != 0:
        print(f"\t\t\t\t\t\t| {daftar_pembelian[menu_nomor][0]}     \t{daftar_pembelian[menu_nomor][1]} Gelas  :   Rp {daftar_pembelian[menu_nomor][2]}\t    |")
        return

# Perulangan untuk menjalankan program selama-lamanya sampai pesanan == False
while (pesanan == True):
    daftar_pembelian = [0 for i in range(len(menu_makanan) + len(menu_minuman))] # Membuat array kosong untuk makanan yang akan dibeli
    total_harga = 0 # Variabel tagihan dibuat nol pada setiap nomor pesanan
    makanan_dipesan = 0 # Jumlah semua makanan yang dipesan
    minuman_dipesan = 0 # Jumlah semua minuman yang dipesan

    program_makan = True # Boolean berjalannya program pesan makanan
    program_minum = True # Boolean berjalannya program pesan minuman

    # Menampilkan menu makanan dan minuman resto beserta harganya
    print("\t\t\t\t|=======================================================================================|")
    print("\t\t\t\t|                            Selamat Datang di Kafe Kompeng 23!                         |")
    print("\t\t\t\t|=======================================================================================|")
    print("\t\t\t\t|     ✦     Daftar Menu Makanan     ✦       |     ✦     Daftar Menu Minuman     ✦       |")
    print("\t\t\t\t|===========================================|===========================================|")
    print("\t\t\t\t|  1. Soft Cookies            Rp 15.000,00  |  1. Americano               Rp 18.000,00  |")
    print("\t\t\t\t|  2. Croissant               Rp 19.000,00  |  2. Cappucino               Rp 23.000,00  |")
    print("\t\t\t\t|  3. Cheese Shortcake        Rp 23.000,00  |  3. Caffe Latte             Rp 25.000,00  |")
    print("\t\t\t\t|  4. Tiramisu Cake           Rp 28.000,00  |  4. Caffe Macchiato         Rp 22.000,00  |")
    print("\t\t\t\t|  5. Kue Pancong             Rp 10.000,00  |  5. Hot Chocolate           Rp 30.000,00  |")
    print("\t\t\t\t|  6. Fried Banana            Rp 18.000,00  |  6. Chamomile Tea           Rp 24.000,00  |")
    print("\t\t\t\t|  7. Spaghetti               Rp 33.000,00  |  7. Earl Grey Tea           Rp 21.000,00  |")
    print("\t\t\t\t|  8. Fettuccine              Rp 30.000,00  |  8. Green Tea               Rp 28.000,00  |")
    print("\t\t\t\t|  9. Panna Cotta             Rp 28.000,00  |  9. Tipsy Ice               Rp 25.000,00  |")
    print("\t\t\t\t|  10. Choux Pastry           Rp 16.000,00  |  10. Sweet Iced Tea         Rp 10.000,00  |")
    print("\t\t\t\t|=======================================================================================|")
    print()

    pertanyaan_makan = input("Apakah Anda ingin memesan makanan? (Ya/Tidak) ") # Jika dijawab tidak, akan langsung ke pesan minuman
    if (pertanyaan_makan == "Tidak"):
        program_makan = False
    elif (pertanyaan_makan == "Ya"):
        program_makan = True

    while (program_makan == True): # Perulangan untuk membeli lebih dari satu jenis makanan
        pesan_makanan = int(input("Pilih makanan yang ingin Anda pesan (1-10): "))
        jumlah_porsi = int(input("Masukkan jumlah porsi yang Anda inginkan: "))
        pesan_makan(pesan_makanan, jumlah_porsi)
        if (jumlah_porsi <= stok_makanan[pesan_makanan-1]):
            total_harga += jumlah_porsi * harga_makanan[pesan_makanan-1] # Menghitung total harga secara kumulatif
        makanan_dipesan += 1
        stop_makan = input("Apakah Anda masih ingin memesan makanan? (Ya/Tidak) ")
        if stop_makan == "Tidak":
            program_makan = False
            print() # Memberi sedikit jeda antara pemesanan makanan dan minuman

    pertanyaan_minum = input("Apakah Anda ingin memesan minuman? (Ya/Tidak) ")
    if (pertanyaan_minum == "Tidak"):
        program_minum = False
    elif (pertanyaan_minum == "Ya"):
        program_minum = True

    while (program_minum == True): # Perulangan untuk jika membeli lebih dari satu jenis minuman
        pesan_minuman = int(input("Pilih minuman yang ingin Anda pesan (1-10): "))
        jumlah_gelas = int(input("Masukkan jumlah gelas yang Anda inginkan: "))
        pesan_minum(pesan_minuman, jumlah_gelas)
        if (jumlah_gelas <= stok_minuman[pesan_minuman-1]):
            total_harga += jumlah_gelas * harga_minuman[pesan_minuman-1] # Menghitung total harga tagihan secara kumulatif
        minuman_dipesan += 1
        stop_minum = input("Apakah Anda masih ingin memesan minuman? (Ya/Tidak) ")
        if stop_minum == "Tidak":
            program_minum = False
            print()

    # Menampilkan daftar pembelian beserta jumlah tagihan yang harus dibayar
    print("\t\t\t\t\t\t|===================================================|")
    print("\t\t\t\t\t\t|            ✦     Daftar Pembelian     ✦           |")
    print(f"\t\t\t\t\t\t|                  Nomor Pesanan : {nomor_pesanan}                |")
    if (makanan_dipesan > 0):
        print("\t\t\t\t\t\t|===================================================|")
        print("\t\t\t\t\t\t|               *      Makanan      *               |")
    for i in range(len(menu_makanan)):
        bill_makan(i)
    if (minuman_dipesan > 0):
        print("\t\t\t\t\t\t|===================================================|")
        print("\t\t\t\t\t\t|               *      Minuman      *               |")
    for i in range(len(menu_makanan), len(menu_minuman)+len(menu_makanan)):
        bill_minum(i)
    print("\t\t\t\t\t\t|===================================================|")
    print(f"\t\t\t\t\t\t| Total harga   \t\t :   Rp {total_harga}\t    |")
    print(f"\t\t\t\t\t\t| Pajak (10%)   \t\t :   Rp {total_harga // 10}\t    |")
    print(f"\t\t\t\t\t\t| Total tagihan   \t\t :   Rp {total_harga * 110 // 100}\t    |")
    sum_pendapatan += total_harga
    print("\t\t\t\t\t\t|===================================================|")
    jeda = str(input("Tekan ENTER untuk melanjutkan "))
    print()
    # Menampilkan metode-metode pembayaran yang dapat digunakan
    print("\t\t\t\t\t\t|===================================================|")
    print("\t\t\t\t\t\t|          ✦   Pilih Metode Pembayaran   ✦          |")
    print("\t\t\t\t\t\t|===================================================|")
    print("\t\t\t\t\t\t|\t      1. Tunai  \t  3. Kredit\t    |")
    print("\t\t\t\t\t\t|\t      2. Debit  \t  4. QRIS\t    |")
    print("\t\t\t\t\t\t|===================================================|")
    print()
    metode_pembayaran = int(input("Pilih metode pembayaran (1-4): "))
    if (metode_pembayaran == 1):
        uang_tunai = int(input("Masukkan jumlah uang tunai: "))
        while uang_tunai < (total_harga * 110 // 100):
            print(f"Jumlah uang tunai tidak mencukupi pembayaran tagihan. Uang Anda kurang Rp {total_harga * 110 // 100 - uang_tunai}")
            uang_tunai = int(input("Masukkan jumlah uang tunai: "))
        print(f"Kembalian Anda sejumlah Rp {uang_tunai - (total_harga * 110 // 100)}")
        print("Pembayaran berhasil")
    elif (metode_pembayaran == 2):
        print("Silakan masukkan kartu debit Anda")
        print("Pembayaran Anda sedang diproses...")
        print("Pembayaran berhasil")
    elif (metode_pembayaran == 3):
        print("Silakan masukkan kartu kredit Anda")
        print("Pembayaran Anda sedang diproses...")
        print("Pembayaran berhasil")
    elif (metode_pembayaran == 4):
        print("Silakan scan QRIS yang tertera")
        print("Pembayaran Anda sedang diproses...")
        print("Pembayaran berhasil")
    print()
    print("Bill sedang dicetak...")
    print("Terima kasih! Selamat menikmati.")
    print()
    print("\t\t\t\t\t\t|=============== Pelanggan Berikutnya ==============|") # Menandai selesainya pelanggan sebelumnya dan memulai pesanan dengan pelanggan yang baru
    print()
    stop_pesanan = input("Apakah Anda ingin memesan? (Ya / Tidak) ") # Jika tidak, maka program berakhir
    if stop_pesanan == "Tidak":
        pesanan = False
        print("\t\t\t\t\t\t|===================================================|")
        print(f"\t\t\t\t\t\t|    Jumlah pesanan hari ini adalah {nomor_pesanan} pesanan\t    |") # Menampilkan banyaknya pesanan
        print(f"\t\t\t\t\t\t|   Total pendapatan hari ini adalah Rp {sum_pendapatan}\t    |") # Menampilkan total pendapatan (kotor)
        print("\t\t\t\t\t\t|===================================================|")
    nomor_pesanan += 1 # nomor pesanan bertambah apabila ada pelanggan berikutnya