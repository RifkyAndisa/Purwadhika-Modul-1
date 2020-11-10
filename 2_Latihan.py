#Soal 1

# harga = 3000
# belanja = int(input('Masukan Jumlah Pisang yang anda inginkan : '))
# total_belanja = harga*belanja
# diskon1 = int(total_belanja * 0.1)
# diskon2 = int(total_belanja * 0.05)

# if total_belanja >= 100000:
#     print (f"total Belanja anda adalah {total_belanja - diskon1} dengan diskon 10%")
# elif total_belanja >= 50000 and total_belanja <= 99000:
#     print (f"total Belanja anda adalah {total_belanja - diskon2} dengan diskon 5%")
# else:
#     print ('Total Belanja Anda Adalah,', total_belanja)


#Soal 2
# lama_kerja = int(input('Sudah Berapa lama anda Bekerja? '))
# gaji = int(input('Berapa Gaji Anda? '))
# bonus = int(gaji * 0.1)

# if lama_kerja > 10:
#     print (f'Selamat Anda Mendapat Gaji! Total Gaji Anda : {bonus + gaji} Dengan Bonus 10%')
# else:
#     print ('Selamat Anda Mendapat Gaji! Total Gaji Anda :', gaji)


#soal 3
# user_1 = int(input('Masukan Umur Anda Di Sini : '))
# user_2 = int(input('Masukan Umur Anda Di Sini : '))
# user_3 = int(input('Masukan Umur Anda Di Sini : '))
# if user_1 > user_2 and user_1 > user_3:
#     print ('User_1 adalah yang paling tua')
# elif user_2 > user_1 and user_2 > user_3:
#     print ('User_2 adalah yang paling tua')
# elif user_3 > user_2 and user_3 > user_1:
#     print ('User_3 adalah yang paling tua')
# else:
#     print('tidak ada yang lebig tua')


#soal 4
kelas = int(input('Total Kelas Yang Di Adakan : '))
absen = int(input('Total Kehadiran : '))
Kehadiran = round(absen / kelas * 100, 2)

if Kehadiran >= 75:
    print(f'Total kehadiran {Kehadiran}%. Anda diperbolehkan mengikuti Ujian')
else:
    print(f'Total Kehadiran {Kehadiran}%. Mohon Maaf, anda Tidak diperbolehkan mengikuti ujian')