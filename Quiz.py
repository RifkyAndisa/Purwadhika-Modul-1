# ------ QUIZ 1 ------

#quis Soalnya 
#bikin input nama dan umur
#tuliskan "halo nama saya .... umur saya 5 tahun kedepan adalah ...."

# nama = input ('Nama Saya ')
# print (nama)
# umur = input ('Umur Saya ')
# print (umur)
# print ('halo nama saya',nama, 'umur saya 5 tahun kedepan adalah',str(int(umur)+5))



# ------ QUIZ 2 ------
 #tentukan Bilangan Ganjil dan genap

# angka = int(input('Masukan Angka di Sini :'))
# if angka % 2 == 0:
#      print ("Maka angka Termaksud Genap")
# else:
#     print ("Maka angka Termaksud Ganjil")


# ---- QUIZ 3, Function ----

# def calculator (angka1, fungsi, angka2):
#     if (isinstance(angka1,int)== True) and (isinstance(fungsi, str)== True) :
#         if fungsi == '+':
#             print (f'hasil pertambahannya dari {angka1}{fungsi}{angka2} adalah {angka1+angka2}')
#             # return (angka1+angka2)
#         elif fungsi == '-':
#             print (f'hasil pengurangannya dari {angka1}{fungsi}{angka2} adalah {angka1-angka2}')
#             # return (angka1-angka2)
#         elif fungsi == '*':
#             print (f'hasil pengaliannya dari {angka1}{fungsi}{angka2} adalah {angka1*angka2}')
#             # return (angka1*angka2)
#         elif fungsi == '/':
#             print (f'hasil pembagiannya dari {angka1}{fungsi}{angka2} adalah {angka1/angka2}')
#             # return (angka1/angka2)
#         elif fungsi == '**':
#             print (f'hasil pemangkatannya dari {angka1}{fungsi}{angka2} adalah {angka1**angka2}')
#             # return (angka1**angka2)
#         else:
#             print(f'Operator {fungsi} tidak dapat ditemukan')
#     else:
#         print('Invalid input')

# calculator (6, '+', 6)


# -- QUIZ 4 Loop --
i = 1 #massukan password, dengan jatah 5 kali salah
password = '12345'

while i <= 5:
    masuk = input ('Masukkan Password: ')
    if masuk != password and i <= 4:
        print ('password incorect')
    elif masuk != password and i <= 5:
        print ('Try Again Later')
    else:
        print ('Password Corect')
        break
    i += 1
