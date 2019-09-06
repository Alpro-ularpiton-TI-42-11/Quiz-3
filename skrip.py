print("Selamat Datang di Telkom Giveaway!")
x = str(input("\nNama Provider : "))
y = float(input("Masukkan IPK : "))

if x == "Telkomsel":
    if y>=3 and y<=4:
        print("Selamat anda mendapatkan Iphone X")
    elif y >=2.75 and y <3:
        print("Selamat anda menddapatkan PS4")
    elif y >=2.25 and y <2.75:
        print("Selamat anda menddapatkan Voucher Oyo")
    else :
        print("\nMaaf anda tidak dapat mengikuti Giveaway ini.\nHarap cek kembali persyaratan untuk mengikuti Giveaway ini.")
else :
    print("\nMaaf anda tidak dapat mengikuti Giveaway ini.\nHarap cek kembali persyaratan untuk mengikuti Giveaway ini.")