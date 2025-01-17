from Cryptodome.Util.number import *

p = getPrime(512)
q = getPrime(512)
n = p*q
x = pow((p+q),2)
r = pow((p-q),2)
what_to_name_dis = x*r
phi = (p-1)*(q-1)
e = 65537
flag = bytes_to_long(b"REDACTED")
d = pow(e, -1, phi)
c = pow(flag, e, n)
print("n = ", n)
print("what_to_name_dis = ", what_to_name_dis)
print("c = ", c)
