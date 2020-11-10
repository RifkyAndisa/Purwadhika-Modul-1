# -- Latihan --
p = {1,2,4,7,9,19}
q = {5,12,16,17,7,9,19,6}
r = {19,6,3,8}
P_Q = p|q
P_R = p|r
Q_R = q|r

print ('gabungan dari P dan Q adalah: ', P_Q)
print ('gabungan dari P dan R adalah:', P_R)
print ('gabungan dari Q dan R adalah:', Q_R)
print ('irisan P_Q dan Q_R adalah: ', P_Q&Q_R)
print ('symetric differen dari Q_R dan P_Q adalah: ', Q_R.symmetric_difference(P_Q))