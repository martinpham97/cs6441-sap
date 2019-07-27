from pwn import *

g = 883
m = 2887
A = 1046
r = remote('plsdonthaq.me', 9001)
r.recvuntil("BEGINING DIFFY HELLMAN KEY EXCHANGE")
r.recvline()
s = r.recvline()
g = int(filter(str.isdigit, s))
s = r.recvline()
m = int(filter(str.isdigit, s))
s = r.recvline()
A = int(filter(str.isdigit, s))
r.recvuntil("Enter yours:")

b = 123
S = pow(g, b) % m

r.sendline(str(S))
r.recvuntil("Enter our secret number:")
r.sendline(str(pow(A,b) % m))
print r.recvline()