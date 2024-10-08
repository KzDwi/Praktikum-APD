user_name = [] #Username untuk User
user_pw = [] #Password untuk User
admin = ["adminkontak","admin1234"] #Login Sebagai Admin
contact = [] #Kontak user akan masuk disini
default_contact = [["Cek nomor","808"],["Layanan Pencegahan Bunuh Diri","119"]] #Kontak khusus yang akan muncul di semua user
start = True #Untuk pengulangan pada menu Kontak Informasi/Kontak Admin

while True :
    print("""
    =============================
    |     MANAJEMEN KONTAK      |
    =============================
    |                           |
    | [1] Login                 |
    | [2] Buat Akun             |
    | [3] Keluar Program        |
    |                           |
    =============================
    """)
    log = int(input("Pilih Fitur [1-3] : "))
    if log == 1:
        i = 0
        while i < 1:
            print("""
        ================
        |    LOGIN     |
        ================
""")
            match_un = input("Masukkan Username :")
            match_pw = input("Masukkan Password :")
            if match_un in user_name and match_pw in user_pw and user_name.index(match_un) == user_pw.index(match_pw):
                print("Login Berhasil!")
                start = True
                while start == True:
                    print("""
        ========================
        |   KONTAK INFORMASI   |
        ========================
        | [1] Tambah Kontak    |
        | [2] Lihat Kontak     |
        | [3] Ubah Kontak      |
        | [4] Hapus Kontak     |
        | [5] Log Out          |
        ========================
""")
                    ans = int(input("Pilih Fitur :"))
                    match ans:
                        case 1:
                            nama = input("Masukkan nama kontak :")
                            nomor = input("Masukkan nomor kontak :")
                            while True:
                                email = input("Tambahkan e-mail? [Y/N]")
                                if email == "Y" or email == "y":
                                    e_mail = input("Masukkan e-mail kontak :")
                                    break
                                elif email == "N" or email == "n":
                                    e_mail = "N/A"
                                    break
                                else:
                                    print("perintah tidak diketahui (hanya Y atau N)")
                            while True:
                                social = input("Tambahkan Akun Sosial? [Y/N]")
                                if social == "Y" or social == "y":
                                    social1 = input("Masukkan akun sosial (contoh : @JohnDoe (Instagram)) :")
                                    break
                                elif social == "N" or social == "n":
                                    social1 = "N/A"
                                    break
                                else:
                                    print("perintah tidak diketahui")
                            print("Kontak Berhasil ditambahkan")
                            contact.append([nama,nomor,e_mail,social1])

                        case 2:
                            for i in range(len(contact)):
                                print(f"Kontak ke-{i+1}\nNama : {contact[i][0]}\nNomor : {contact[i][1]}\nE-mail : {contact[i][2]}\nSocial : {contact[i][3]}\n")
                            print("Kontak lainnya:")
                            i = 0
                            for i in range(len(default_contact)):
                                print(f"Nama : {default_contact[i][0]}\nNomor : {default_contact[i][1]}\n")

                        case 3:
                            for i in range(len(contact)):
                                print(f"Kontak ke-{i+1}\nNama : {contact[i][0]}, Nomor : {contact[i][1]}\n")
                            match_ch = int(input("Pilih kontak yang ingin diubah (hanya angka) :"))
                            match_ch -= 1
                            if match_ch >= 0 and match_ch <= len(contact):
                                new_name = input("Nama :")
                                new_num = input("Nomor :")
                                new_email = input("E-mail :")
                                new_social = input("Social :")
                                contact[match_ch][0] = new_name
                                contact[match_ch][1] = new_num
                                contact[match_ch][2] = new_email
                                contact[match_ch][3] = new_social
                                print("Kontak berhasil diubah")
                            else:
                                print("Kontak tidak ditemukan")

                        case 4:
                            for i in range(len(contact)):
                                print(f"Kontak ke-{i+1}\nNama : {contact[i][0]}, Nomor : {contact[i][1]}\n")
                            match_cdel = int(input("Pilih kontak yang ingin dihapus (hanya angka) :"))
                            match_cdel -= 1
                            if match_cdel >= 0 and match_cdel <= len(contact):
                                del contact[match_cdel]
                                print("Kontak Berhasil dihapus")
                            else:
                                print("Kontak tidak ditemukan")

                        case 5:
                            i = 1
                            break
                        case _:
                            print("Perintah tidak diketahui (Pilih opsi antara 1 sampai 6)")
            elif match_un == admin[0] and match_pw == admin[1]:
                print("Login Berhasil!")
                while start == True:
                    print("""
        ==================================
        |          KONTAK ADMIN          |
        ==================================
        |                                |
        | [1] Tambahkan Kontak Khusus    |
        | [2] Lihat Semua Daftar Kontak  |
        | [3] Ubah Kontak Khusus         |
        | [4] Log Out                    |
        |                                |
        ==================================
""")
                    adm_choose = int(input("Pilih Fitur (1 - 4) :"))
                    match adm_choose:
                        case 1:
                            adm_name = input("Masukkan nama kontak : ")
                            adm_num = input("Masukkan nomor kontak : ")
                            default_contact.append([adm_name,adm_num])
                        case 2:
                            for i in range(len(contact)):
                                print(f"Kontak ke-{i+1}\nNama : {contact[i][0]}\nNomor : {contact[i][1]}\nE-mail : {contact[i][2]}\nSocial : {contact[i][3]}\n")
                            print("Kontak Khusus:")
                            for i in range(len(default_contact)):
                                print(f"Nama : {default_contact[i][0]}\nNomor : {default_contact[i][1]}\n")
                        case 3:
                            for i in range(len(default_contact)):
                                print(f"Nama : {default_contact[i][0]}\nNomor : {default_contact[i][1]}\n")
                            match_adm_ch = int(input("Pilih kontak yang ingin diubah : "))
                            match_adm_ch -= 1
                            if match_adm_ch >= 0 and match_adm_ch <= len(default_contact):
                                new_adm_name = input("Nama : ")
                                new_adm_num = input("Nomor : ")
                                default_contact[match_adm_ch][0] = new_adm_name
                                default_contact[match_adm_ch][1] = new_adm_num
                            else:
                                print("Kontak tidak ada")
                        case 4:
                            print("Keluar dari mode Admin. . .")
                            start = False
                            i = 1
                        case _:
                            print("Perintah Tidak Diketahui (Pilih Antara 1 sampai 4)")
            else:
                print("Login Gagal")
                while True:
                    ul1 = input("Coba lagi? [Y/N] :")
                    if ul1 == "Y" or ul1 == "y" :
                        break
                    elif ul1 == "N" or ul1 == "n" :
                        i = 1
                        break
                    else:
                        print("Perintah tidak ditemukan (Hanya Y/N) ")
    elif log == 2:
        #Proses Buat Akun
        print("Silahkan isi pertanyaan berikut :")
        add_un = input("Masukkan Username :")
        add_pw = input("Masukkan Password :")
        user_name.append(add_un)
        user_pw.append(add_pw)
        print("Akun anda telah dibuat, silahkan pilih opsi login untuk masuk")
    elif log == 3:
        #Quit Program
        break
    else:
        print("Fitur tidak ada (pilih antara 1 dan 3)")