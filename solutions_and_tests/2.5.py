from simplecrypt import decrypt

with open("../files_from_course/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("../files_from_course/passwords.txt", "r") as pas:
    password = pas.read().split('\n')

for pasw in password:
    pasw.strip()
    print(pasw)
    try:
        print(decrypt(pasw, encrypted))
    except:
        continue