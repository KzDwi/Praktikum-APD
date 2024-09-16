nama = input("masukkan nama kamu : ")
nim = input("masukkan nim kamu : ")
harga = float(input("masukkan harga beras : "))

mawar = harga-(harga*11/100)
sania = harga-(harga*14/100)
maknyus = harga-(harga*17/100)

print(nama,"dengan NIM",nim,"ingin membeli beras seharga Rp",harga,"\n","Jika dia membeli beras mawar, ia harus membayar Rp",mawar,"setelah mendapat diskon 11%","\n","Jika dia membeli beras sania, ia harus membayar Rp",sania,"setelah mendapat diskon 14%","\n","Jika dia membeli beras maknyus, ia harus membayar Rp",maknyus,"setelah mendapat diskon 17%")