from pwn import *

r = remote('plsdonthaq.me', 9002)
r.recvuntil("INTERCEPTING DIFFY HELLMAN KEY EXCHANGE")
r.recvline()
s = r.recvline()
g = int(filter(str.isdigit, s))
s = r.recvline()
m = int(filter(str.isdigit, s))
s = r.recvline()
A = int(filter(str.isdigit, s))
s = r.recvline()
B = int(filter(str.isdigit, s))
r.recvuntil("Eve:")

for i in range(10000):
  if int(pow(g,i)%m)==A:
    a = i
    break

r.sendline(str(pow(B,a) % m))
print r.recvline()