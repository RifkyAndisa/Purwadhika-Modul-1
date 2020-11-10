# # --- LIST ---

# mobil = ['Toyota', 'Honda', 'Jaguar']

# print (type(mobil))
# print (mobil)

# #indexing
# print (mobil[0])
# print (mobil[1]) #memanggil sesuai nomor index

# #sliceing
# print (mobil[0:2])
# print (mobil[:3])
# print (mobil[1:])
# print (mobil[::-1])

# #append -- menambahkan daftar pada posisi di paling belakang
# mobil.append('BMW')
# print (mobil)

# #pop -- menghapus element pada posisi paling belakang
# hasil_pop = mobil.pop()
# print (mobil)
# print (hasil_pop)

# # index = mengetahui index dari sebuah element tertentu
# print ('index dari mobil Honda adalah : ', mobil.index('Honda'))
# print ('index dari mobil Jaguar adalah : ', mobil.index('Jaguar'))
# print(mobil[mobil.index('Honda')].index('H')) #Mencari index Di dalam sebuah index kendaraan (index = kamar)

# # copy = meng-copy list
# mobil_copy = mobil.copy()
# print (mobil_copy)
# print (mobil)

# mobil_copy.pop()
# print (mobil_copy)
# print (mobil) #tidak akan terdampak oleh pop dari mobil_copy

# # insert = memasukan element index tertentu
# mobil.insert (0, 'Hummer')
# print(mobil)
# mobil.insert (10, 'Proton')
# print (mobil)
# mobil.insert (2, 'Subaru')

# #sort = mengurutkan  (reverse = True/False)
# mobil.sort(reverse=False)
# print(mobil)

# # reverse = membalik urutan dari listnya
# mobil.reverse()
# print(mobil)

# # count = menghitung ada berapa element di dalam list
# print(mobil.count('Jaguar'))

# #extend = memasukan beberapa element sekaligus
# mobil.extend (['Ferari', 'Audi', 'McLaren'])
# mobil.sort(reverse=False)
# print(mobil)

# #cara memamnggil element di list dalam list
# mobil.append(['BMW', 'Ford'])
# print(mobil)
# print(mobil[9][1]) 

# #cara mengganti element pada index
# # mobil[9] = 'BMW'
# mobil[9][1] = 'Porsche'
# print(mobil)

# #broadcasting mengganti beberapa element sekaligus
# mobil[0:3] = 'Kijang', 'Tesla'
# print(mobil)
# mobil[8], mobil [0] = 'Porsche', 'BMW'
# print(mobil)

# #in = untuk mengecek element tertentu ada di dalam sebuah list
# print('Toyota' in mobil)

# #---Tuple--- = Valuenya tidak bisa di ubah sama sekali, pakai ()
# tidak bisa menggungakan fungsi dari list di atas, namun bisa di jadikan list
# angka = (1,2,3,4,5,6)
# print(type(angka))


# ---SET--- set tidak melakukan indexing/sliceing
# pakai kurung {}
z = {1,2,3,1,2,3,4,4,4,4,4}
print(type(z))
print(z) #hasilnya {1, 2, 3}
z_list = list(z)
print (z_list)
back_to_set = set(z_list)

#add = menambah elemen baru (jika memasukan string maka tidak di pecah)
z.add(5)
print(z)
z.add('Budi')
print(z)

#update = menambahkan elemen sekaligus (jika memasukan string maka akan di pecah per alphabet)
#harus memasukan datanya dalam bentuk itterable (list,tuple,set)
z.update([5,6,7,8,])
print(z)
z.update ('Andy')
print (z)

#discard = menghapus 1 element tertentu
z.discard('Budi')
print(z)

#pop = menghilangkan 1 element tertentu (secara random)
z.pop()
print('pop pertama', z)
z.pop()
print ('pop kedua', z)

#clear = menghapus semua element di dalam set
# z.clear()
# print(z)

a = list('abcdeaaaaaa')
b = list('bcfga')
c = ['halo', 'apa', 'kabar']
c_join = ' '.join(c) #menggabungkan kata menjadi kalimat
print (c_join)
print(a,b)

a_set = set(a)
b_set = set(b)
print(a_set, b_set)
# -Intersection / irisan-
print ('irisan atau intersection dari set_a dan set_b: ', a_set.intersection(b_set)) #menentukan irisan
#atau
print ('irisan atau intersection dari set_a dan set_b: ', a_set&b_set) #menentukan irisan

# -difference / selisih-
print ('selisih atau diference dari set_a dan set_b: ', a_set.difference(b_set)) #selisih dari a_set
print ('selisih atau diference dari set_b dan set_a: ', b_set.difference(a_set)) #selisih dari b_set
#atau
print ('selisih atau diference dari set_b dan set_a: ', b_set-a_set) #selisih dari b_set

# -UNION-
print ('gabungan atau union dari set_a dan set_b: ', a_set.union(b_set)) #gabungan dari semuanya
#atau
print ('gabungan atau union dari set_a dan set_b: ', a_set|b_set) #gabungan dari semuanya

# -Beda setangkup / symetric-
print ('beda setangkup atau symetric difference set_adan set_b: ',a_set.symmetric_difference(b_set)) #selisih dari a_set dan b_set
