import crypt

def crackPass(encrypted_password, dictionary):
  salt = encrypted_password[:3] + encrypted_password.split("$")[2]

  with open(dictionary,'r') as d:
    for word in d.readlines():
      word = word.strip('\n')
      word_capt = word.capitalize()
      word_rev = word[::-1]
      word_capt_rev = word.capitalize()[::-1]

      if crypt.crypt(word, salt) == encrypted_password:
        return word
      elif crypt.crypt(word_capt, salt) == encrypted_password:
        return word_capt
      elif crypt.crypt(word_rev, salt) == encrypted_password:
        return word_rev
      elif crypt.crypt(word_capt_rev, salt) == encrypted_password:
        return word_capt_rev

  return None

def main():
  captured = "passwords.txt"
  dictionary = "google-10000-english.txt"

  with open("passwords.txt") as f:
    for line in f:
      if ":" in line:
        tokens = line.split(":")

        user = tokens[0]
        encrypted_password = tokens[1]

        print("[*] Cracking Password For: {}".format(user))

        decrypted_password = crackPass(encrypted_password, dictionary)

        if decrypted_password:
          print("[+] Found Password: {}".format(decrypted_password))
        else:
          print("[-] Password Not Found")


if __name__ == "__main__":
  main()