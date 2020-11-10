# LATIHAN 1
# x = 4
# y = 3
# z = 2
# print(((x+(y*x))/(x*y))**z)

# # #LATIHAN 2
# angka = input ('Silahkan Masukan Angka Berapapun : ')
# int_angka = int(angka)
# print('kuadrat dari', int_angka, '=', (int_angka**2))

# #LATIHAN 3
# a = input ('Jumlah Hari :')
# a_int = int(a)
# tahun = a_int // 360
# bulan = (a_int % 360)//30
# Minggu = (a_int % 30)//7
# hari = (a_int % 30)% 7
# print (tahun,'Tahun', bulan,'Bulan',Minggu,'Minggu', hari,'Hari') 

# #LATIHAN 4
# andi = (4*49)//(4+10)
# budi = 49 - andi
# print(andi+2, budi+2)

#LATIHAN 5
# x = input('kata apapun di kolom sini : ').lower()
# y = input (f"masukan Huruf yang mau di cari dari '{x}': ").lower()
# z = x.replace(y, '')
# print(f'Huruf {y} ada {len(x)-len(z)} dalam kalimat {x}')

# #LATIHAN 6
# jarak = 120
# kecepatan_A = 60
# kecepatan_B = 40
# start = 9
# time = (jarak / (kecepatan_A + kecepatan_B))*60
# waktu = int(time // 60)
# menit = int(time % 60)
# print('jam', waktu + start, 'lewat', menit, 'menit' )