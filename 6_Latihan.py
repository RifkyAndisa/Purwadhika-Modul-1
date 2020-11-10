# 1
# i = 0
# n = int(input ('masukan angka : '))
# while i <= n:
#     if i %3 == 0 and i %5 == 0:
#         print ('Fizz Buzz')
#     elif i %5 ==0:
#         print ('Buzz')
#     elif i %3 == 0:
#         print ('Fizz')
#     else : 
#         print (i)
#     i += 1

# 2 reverse anga yang di input
# d = list (input ('MASUKAN ANGKA CANTIK : '))
# i = 0
# e = []
# for i in range(len(d)):
#     k = -(i+1) 
#     e.append(d[k])

# print(e)


# 4
a = int(input('MASUKAN JUMLAHNYA BERAPA : '))
z=''
for b in range(a):
    for b1 in range (0, b+1):
        z += ' * '
    z += '\n'

# print (z)

#5
a = int(input('MASUKAN JUMLAHNYA BERAPA : '))
z=''
for b in reversed(range(a)):
    for b1 in range (0, b+1):
        z += ' * ' 
    z += '\n'

print(z)

# or
a =int(input("Masukkan angka tersera bro"))

for b in reversed(range (0,a)):
    for b1 in range(0, b):
        print("*", end="")
    print("*")

# 6
a = int(input('MASUKAN JUMLAHNYA BERAPA : '))
z=''
for b in reversed(range(a)):
    for b1 in range (0, b+1):
        z += '*' 
    z += '\n'
for b in range(a):
    for b1 in range (0, b+1):
        z += '*' 
    z += '\n'

# print(z)