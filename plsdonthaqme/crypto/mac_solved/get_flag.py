import hashlib
import re
from pwn import *

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

key_text="This round's shared key is"
send_text="Send me a message:"
mac_text="Enter your MAC:"
response_text="Response:\n"
lying_text="But I could be lying, check that the following MAC hash equals the following:"

r = remote('plsdonthaq.me', 9004)

while True:
  r.recvuntil(key_text)
  r.recvline()
  key = r.recvline()
  key = escape_ansi(key.rstrip())
  r.recvuntil(send_text)
  r.recvline()

  # server will go through the actual flag
  # if the next message has the character in the flag
  # then it will give the correct flag for the next word
  # if the message doesnt have the character, it will
  # lower the chance of getting the correct flag letter
  # until the chances of getting any correct letter is 0
  text = "COMP6441\{n0w_yoU_kNow_hOw_MaCs_WorK_nice_pRogr4mMing\}"
  text_hashed = encrypt(key, text)

  r.sendline(text)
  r.recvline()
  r.sendline(text_hashed)
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
  flag_hashed = r.recvline()
  flag_hashed = flag_hashed.rstrip()

  if str(encrypt(key, flag)) == flag_hashed:
    print(flag)
    
    # cat capture.txt | sort -n -k 4,4 | uniq 
    with open("capture.txt", "a+") as myfile:
      myfile.write(flag+'\n')