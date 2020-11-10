# -- DICTIONARY --
# ada 2 element, key dan value

employee = {
    'nama': 'Andy', 
    'usia' : '20',
    'married' : True,
    'jabatan' : 'IT Engineer',
    'kendaraan': ['mobil','motor'],
    'alamat' : {
        'street' : 'jalan mawar',
        'RT' : 5,
        'RW' : 2,
        'zipcode' : 12345,
        'geo' : {
            'lat' : 12345.6789,
            'long' : 1234.1234,
        }
    }
}
print (employee) #memanggil semua data yang ada di dictionary
print (employee['kendaraan']) #memanggil value dalam key 
print (employee['kendaraan'][0]) #memanggil value dalam list
print (employee['alamat']['RT'])

# --GET--
print (employee.get('gaji', 'Tidak Dapat Di Temukan')) #mengambil value dalam key ( dan dapat di kasih pesan jika tidak di temukan)

# -- Assign Value baru ke Key yang baru juga --
employee['gaji'] = 2000000
print (employee)

# -- Update Value di key yang sudah ada ---
employee['gaji'] = 3000000
print (employee)
employee['kendaraan'].append('sepeda') # di tambahkan ke dapalam value
print(employee)
# -- .update untuk mengupdate tapi dapat mengupdate beberapa key sekaligus --
employee.update({'NIK' : 92131231, 'BPJS' : 10000002121})
print (employee)

# -- .items untuk melihat pasangan antara key dan valuenya --
print (list(employee.items()))
print (list(employee['alamat'].items()))
print (list(employee['alamat']['geo'].items()))

# -- cari value ada di dictionary atau tidak --
print('cari value 3.000.000 ada atau tidak? ', 3000000 in employee.values())

# -- cari value terkecil di dalam dictionary ---

nilai = {
    'Fisika' : 82,
    'Matematika' : 65,
    'Sejarah' : 75
}
print('mata pelajaran yang nilainya paling kecil :', min(nilai, key=nilai.get), 'dengan nilai yang di dapat : ', min(nilai.values()))
print('mata pelajaran yang nilainya paling tinggi :', max(nilai, key=nilai.get), 'dengan nilai yang di dapat : ', max(nilai.values()))

# -- Mengganti nama key --
employee['address'] = employee.pop('alamat')
print(employee)

# --- Menggabungkan dua dictionary ----
dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
dict2 = {'Forty' : 40, 'Fifty' : 50, 'Sixty' : 60}

# cara ke-1 .update
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
#cara ke-2
dict1_dict2 = {**dict1, **dict2}
print (dict1_dict2)

# membuat dictinary dari 2 buah list, bisa di gunakan berbagai macam jenis data
# list, Tuple, list...
key = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]

sample_dict = dict(zip(key, value)) #zip di gunakan untuk menggabungkan itterable dengan itterable yang lainnya hailnya tuple jika di pakai dengan list / tuple

# --initialize dictionary with deafult values--
karyawan = ['doni', 'fikri', 'akbar']
defaults = {'designation' : 'application developer', 'salary' : 5000000}

res_dict = dict.fromkeys(karyawan, defaults)
print (res_dict)
print (res_dict['doni'])