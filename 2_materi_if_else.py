# x = 5
# y = '5'
# z = 6

# ---Conditional Statement---
# print (x == float(y)) #sama dengan
# print (x == z)
# print (x != z) #tidak sama dengan
# print (x > z) #lebih besar
# print (x < z) #lebih kecik
# print (x >= z) #lebih besar sama dengan
# print (x <= z) #lebih kecil sama dengan

#and atau or
#     False and True = False
# print (x == z and x < z)
#     False or True = True
# print (x == z or x < z)

# -- Rules AND --
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# -- Rules Or --
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# -- IF, Else --

# nilai = int(input ('Masukan Nilai : '))

# if nilai >= 80:
#     print ('LULUS')
# else:
#     print ('Remedial')

# if nilai >= 80 and nilai <= 100:
#     print ('A')
# elif nilai >= 70 and nilai <=80:
#     print ('B')
# else:
#     print('C')


# Tentukan Berat badan
bb = input('Masukan Berat Badan Anda :')
tb = input('Masukan Tinggi Badan Anda : ')
if bb.isnumeric() == False or tb.isnumeric () == False:
    print('Tolong Masukan hanya Angka')
else:
    bb = int(bb)
    tb = int(tb)
    imt = round(((bb / tb)/tb)*10000, 2)
    print (f"{imt} Berat Badan {bb} kg dan Tinggi badan {tb / 100} m")

    if imt < 18.5:
        print ('Berat Badan Kurang')
    elif imt >= 18.5 and imt <= 24.9:
        print ('Berat Badan Ideal')
    elif imt >= 25 and imt <= 29.9:
        print ('Berat Badan Lebih')
    elif imt >= 30 and imt <= 39.9:
        print ('Berat Badan sangat Berlebih')
    else:
        print ('obesitas')

#isaplha == string mengandung alphabet only
#isalnum == string mengandung alpha-numeric
#isnumeric == string mengandung numeric only