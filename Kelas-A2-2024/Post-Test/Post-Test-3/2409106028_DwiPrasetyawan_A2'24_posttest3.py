nama = input("masukkan nama kamu : ")
nim = input("masukkan nim kamu : ")
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

