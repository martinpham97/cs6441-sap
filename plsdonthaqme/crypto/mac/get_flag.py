import datetime
import hashlib
from pwn import *
import re
import time

def escape_ansi(line):
  ansi_regex = r'\x1b(' \
             r'(\[\??\d+[hl])|' \
             r'([=<>a-kzNM78])|' \
             r'([\(\)][a-b0-2])|' \
             r'(\[\d{0,2}[ma-dgkjqi])|' \
             r'(\[\d+;\d+[hfy]?)|' \
             r'(\[;?[hf])|' \
             r'(#[3-68])|' \
             r'([01356]n)|' \
             r'(O[mlnp-z]?)|' \
             r'(/Z)|' \
             r'(\d+)|' \
             r'(\[\?\d;\d0c)|' \
             r'(\d;\dR))'
  ansi_escape = re.compile(ansi_regex)
  return ansi_escape.sub('', line)

def encrypt(key, text):
  return hashlib.sha1(key+text).hexdigest()

lying_text="But I could be lying, check that the following MAC hash equals the following:"
key_text="This round's shared key is"
send_text="Send me a message:"
mac_text="Enter your MAC:"
flag_text="flag[93m#[92m#[91m#[0m"
response_text="Response:\n"

# keys = ['palm_leaves', 'susageP','skeletor','monkey','segfault','basement','sausage', 'helicopters', 'skeletor', 'bananarama']

r = remote('plsdonthaq.me', 9004)

while True:
  r.recvuntil(key_text)
  r.recvline()
  key = r.recvline()
  key = escape_ansi(key.rstrip())
  r.recvuntil(send_text)
  r.recvline()
  print(key)
  text = key
  e = encrypt(key, text)
  r.sendline(text)
  r.recvuntil(mac_text)
  r.recvline()
  r.sendline(e)
  r.recvline()
  r.recvuntil(response_text)
  r.recvline()
  flag = r.recvline()
  flag = escape_ansi(flag.rstrip())
  flag = flag.translate(None, '###')
  r.recvuntil(lying_text)
  r.recvline()
  r.recvline()
  r.recvline()
  h = r.recvline()
  h = h.rstrip()
  if str(encrypt(key, flag)) == h:
    print flag
    # keys.append(key[::-1])
    # keys.append(key)
    with open("a.txt", "a") as myfile:
      myfile.write(flag+'\n')