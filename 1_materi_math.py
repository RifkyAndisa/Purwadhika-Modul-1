print('Hello World!')
    #Fungsi Print adalah mencetak sesuatu

nama = 'Rifky' #data type string
umur = 24 #data Type integer (tidak usah pakai petik)
pekerjaan = 'Barista'
    #Nama, Umur, Pekerjaan itu variabel. dan variabel di gunakan untuk data yang akan di gunakan berulang
print(nama)
print(umur,pekerjaan)

dtype_nama = type(nama) # - <class STR>
dtype_umur = type(umur) # - <class int>
    #type di gunakan untuk megecek jenis datanya (integer/string)
print(dtype_umur, dtype_nama)

    #Fungsi Input, untuk meng input data
nama = input('what is your name :') #data tipe akan selalu berbentuk string
print('Hello my name is', nama) #kalo pakai "," tidak perlu pakai spasi
print('hello my name is ' + nama) #kalau pakai "+" jangan lupa pakai spasi "sebelum kutip tutup"

    #Perhitungan matematika
print (2 + 1)
print (2 - 1)
print (3 * 2)
print (4 / 2) #hasilnya 2.0 typenya Float (menggunakan desimal)
print (4 // 2) #hasilnya 2 typenya int 
print (5 % 2) #Modulo Sisa pembagian
print (3 ** 4) #pemangkatan

    #mengganti data type
x = '10'
print(int(x))
print (type(x))
y = int(x)
print (y)
print (type(y))
    #str to int

z = '2.3'
print (float(z))
print(type(z))
# or
z_float = float(z)
print(z_float)
print(type(z_float))
    #str to float

a = 1.2
print (str(a))
print (type(a))
#or
a_str = str(a)
print (a_str)
print (type(a_str))
    #float to str


    #Meng Update
usiaAndi = 30
# usiaAndi = usiaAndi + 5
# usiaAndi /= 2
# usiaAndi *= 2
print (usiaAndi)


import math #cara 1 (import math)

print (math.pi)
print (math.fabs(-23.2)) #menghilangkan negatif
print (math.pow(3, 4)) #pemangkatan
print (math.sqrt (25)) #akar
print (math.ceil(2.5)) #membulatkan ke atas
print (math.floor(2.5)) #membulatkan ke bawah
print (round(5.54554452, 2)) # membulatkan dengan desimal (tergantung mau berapa angka di belakang koma)

# --- STRING ---

x ='Halo Dunia Lain'
print (x)
print (type(x))
print (len(x)) #menghitung ada berapa elemen huruf di dalam string
print (x.index('L')) #mencari elemen ada di kamar nomor berapa (index)
print (x.split()) #di pisah dan menjadikan sebua list base on yg kita input (bila tidak base on spasi)
print (x.lower()) #membuat semua jadi huruf kecil
print (x.upper()) #membuat menjadi huruf besar semua
print ('halo dunia lain'.capitalize()) #membuat huruf capital
print (x.replace('Lain', 'Baru')) #mengganti sebuah elemen

# --- INDEXING / SLICEING ---
print(x[0]) #melihat di dalam index ada elemen apa
print(x[2])
print(x[-1]) #mengaksise elemen yang berada di index terakhir
print(x[-15])
print(x[0:4]) #SLICE ING (angka dari index ke berapa sampai ke berapa)
print(x[5:15])
print(x[x.index('D'):]) #cara lain sliceing dari "D" sampai terakhir
print(x[:x.index('L')])

# --- BOOLEAN ---
jomblo = False
print(jomblo)
print(True+False)
print(True+True)
print(False+False)