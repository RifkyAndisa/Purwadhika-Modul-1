# f(x) = 2x + 3
# f(3) = 2(3) + 3
# f(3) = 9

# --- Function 1 parameter ---
# function hello world
def hello() : #harus mengawali dengan def
    print("Hello World") 

hello ()

#function pangkat 2
def power():
    print (3**2)

power()

 
def power2(x):
    print('print dari dalam function', x**2) #hasil dari print di dalam tidak bisa di masukan ke dalam variabel
    return (x**2) #harus pakai return untuk bisa di masukan ke dalam variabel
# power2(x) #nilai x harus di masukan di sini
hasil = power2(4)
print('print dari luar function', hasil)

# ---Function 2 paramete---
def power3 (angka, pangkat):
    return (angka**pangkat)

hasil_power3 = power3(2, 10)
print ('Hasil dari 2 pangkat 10 adalah : ', hasil_power3)