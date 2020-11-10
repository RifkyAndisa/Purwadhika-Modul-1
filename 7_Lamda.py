## LAMBDA ## (anonymus function)
#di gunakan untuk function yang sederhana#

def perkalian (a, b):
    print (a*b)
perkalian (2, 3) #hasilnya 6

x = lambda a, b: a* b
print (x(2,3)) #hasilnya 6

y = lambda a, b, c : (a/b)*c
print(y(1,2,3)) #hasilnya 1,5

# else if dalam lambda #
z = lambda a :'Genap' if a%2 == 0 else 'Ganjil'
print(z(4)) #hasilnya Genap
print(z(3)) #hasilnya Ganjil

#lambda di dalam def#
def penjumlahan (a, b):
    y = lambda a,b : a+b
    return y(a,b)
print (penjumlahan(1,2)) #hasilnya 3

## MAP ##
name_list= 'Andi Budi Caca'.split()
def function(a):
    return len(a)

len_list = list(map(function, name_list)) #hasilnya [4, 4, 4]
print (len_list)

len_list2= list(map(lambda a : len(a), name_list)) #hasilnya [4, 4, 4]
print (len_list2)

list_1 = 'cokelat melon nangka'.split()
list_2 = [10000, 5000, 20000]
couple_list = list(map(lambda a, b : a + str(b), list_1, list_2))
print (couple_list) #hasilnya ['cokelat10000', 'melon5000', 'nangka20000']

## FILTER ##
h = range(11) #[0,1,2,3,4,5,6,7,8,9,10]
def kurang_lima(x):
    if x < 5:
        return True
    else :
        return False
j = list(filter(kurang_lima, h))
print(j) #hasilnya [0, 1, 2, 3, 4]
print(list(h)) #hasilnya [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = [1,2,3,4,5]
i = [1,2,6,7,8]

m = list(filter(lambda a: a not in k, i))
print(m) #hasilnya [6, 7, 8]

# LATIHAN #

''' pakai MAP dan Lambda 
input = [2,4,6,8]
output = [4,16,36,64]
'''
i_1 = [2,4,6,8]
i_2 = list(map(lambda a : a**2, i_1))
print (i_2) # hasilnya [4, 16, 36, 64]

'''
'''
#QUIZ 
q = ['merdeka','hello','sohib','kari ayam','pesawat','mobil','loker','kamar','saya','motor','pertamax','merah']
q_search = str(input ('what do you want to search: '))

hasil = list(filter(lambda a : q_search in a, q))
print (list(hasil))

'''
'''
# REDUCE #
from functools import reduce

numbers = [6,2,3,4,5]
numbers_sum = reduce(lambda a, b : a+b, numbers)
print (numbers_sum) #hasilnya 20

kata = ['ini','ibu','budi']
kata_reduce = reduce(lambda a, b : a+b, kata)
print (kata_reduce) #hasilnya iniibubudi

#QUIZ 2#
'''
input = [1-100]
output = [5100]

rules = bilangan genap semua, di kalikan 2, di jumlah semua
challenge = kalo bisa cuma 1 line
clue = pakai reduce, filter, map
'''
# an = list(range(1, 101))
# gen = list(filter(lambda a : a % 2 == 0, an))
# k_2 = list (map(lambda a: a * 2, gen))
# hasil = reduce (lambda a, b : a+b, k_2) 
print(reduce (lambda a, b : a+b, (list(map(lambda a: a*2, (filter(lambda a : a% 2 == 0, (range(1,101)))))))))