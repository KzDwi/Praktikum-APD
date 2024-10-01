i = 3
login = False
ulang = True
while ulang == True :
    while i > 0 :
        username = input("Masukkan Username (tanpa kapital) :")
        password = input("Masukkan Password (tidak perlu masukkan angka 0 di awal) :")
        if username == "dwi" and password == "28" :
            print("Login berhasil!")
            login = True
            i = 0
            break
        else:
            print("Percobaan Login gagal!")
            i -= 1
            print(f"sisa percobaan : {i}")
    if i == 0 and login == False:
        print("Percobaan Login Telah Habis!")
        break
    else:
        nama = input("Masukkan nama peminjam :")
        nim = int(input("Masukkan NIM peminjam :"))
        pinjaman = float(input("Masukkan nominal yang ingin dipinjam : "))
        durasi = int(input("Masukkan durasi peminjaman (hitungan tahun) : "))
        if pinjaman >= 0 :
            if durasi == 1 :
                bunga = 7/100
                bulanan = (bunga/12)*pinjaman
                cicilan = (pinjaman + bulanan) / (durasi*12)
                print(f"{nama} dengan nim {nim} meminjam uang sejumlah Rp {pinjaman} dengan durasi peminjaman {durasi} tahun, maka Cicilan perbulannya adalah Rp {cicilan}")
            elif durasi == 2 :
                bunga = 13/100
                bulanan = (bunga/12)*pinjaman
                cicilan = (pinjaman + bulanan) / (durasi*12)
                print(f"{nama} dengan nim {nim} meminjam uang sejumlah Rp {pinjaman} dengan durasi peminjaman {durasi} tahun, maka Cicilan perbulannya adalah Rp {cicilan}")
            elif durasi == 3 :
                bunga = 19/100
                bulanan = (bunga/12)*pinjaman
                cicilan = (pinjaman + bulanan) / (durasi*12)
                print(f"{nama} dengan nim {nim} meminjam uang sejumlah Rp {pinjaman} dengan durasi peminjaman {durasi} tahun, maka Cicilan perbulannya adalah Rp {cicilan}")
            else:
                print("Mohon maaf, durasi peminjaman anda diluar 1 - 3 tahun")
        else:
            print("Jumlah peminjaman tidak bisa kurang dari nol")
        while True:
            kembali = input("Mau ulang menghitung lagi? [Y/N] :")
            if kembali == "y" or kembali == "Y" :
                break
            elif kembali == "n" or kembali == "N" :
                home = input("Kembali ke sesi login? [Y/N] :")
                if home == "y" or home == "Y" : 
                    i = 3
                    break
                elif home == "n" or home == "N" : 
                    print(f"Sampai jumpa lagi, {username}!")
                    ulang = False
                    break
                else:
                    print("Silahkan masukkan antara Y/N")
            else:
                print("Silahkan masukkan antara Y/N")