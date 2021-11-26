def encrypt(bytesOfLenKeyPls, keyPls):
    encrypted_text = ""
    if len(bytesOfLenKeyPls) < len(keyPls):
        bytesOfLenKeyPls = '\0' * (len(keyPls) - len(bytesOfLenKeyPls)) + bytesOfLenKeyPls

    for i in ['0' * (10 - len(bin(ord(a) ^ ord(b)))) + bin(ord(a) ^ ord(b))[2:] for a, b in
              zip(bytesOfLenKeyPls, keyPls)]:
        encrypted_text += i + ' '
    return encrypted_text


def decrypt(bytesOfLenKey, key):
    decrypted_text = ""
    for x, y in zip(bytesOfLenKey.split(), key.split()):
        character = (bin(int(x, base=2) ^ int(y, base=2))[2::])
        if chr(int(character, base=2)) != '\0':
            decrypted_text += chr(int(character, base=2))
    return decrypted_text


print("Introduceti cheia pentru criptare:", end=" ")
key = input()
# key = "4RyAZ9aJ7m5s"
print("Introduceti textul pe care doriti sa-l criptati:", end=" ")
text_to_encrypt = input()
key_length = len(key)
text_length = len(text_to_encrypt)
encrypted_text = ""
encrypted_key = ""
decrypted_text = ""
for ch in key:
    if (len(bin(ord(ch))[2::]) < 8):
        encrypted_key += '0' * (8 - len(bin(ord(ch))[2::]))
    encrypted_key += bin(ord(ch))[2::] + ' '
while text_length > 0:
    encrypted_text += encrypt(text_to_encrypt, key)
    text_to_encrypt = text_to_encrypt[key_length::]
    text_length -= key_length
print("Cheia criptata este:", encrypted_key)
print("Textul criptat in binar este: ", encrypted_text)
encrypted_text_length = len(encrypted_text)
encrypted_key_length = len(encrypted_key)
while encrypted_text_length > 0:
    decrypted_text += decrypt(encrypted_text, encrypted_key)
    encrypted_text = encrypted_text[encrypted_key_length::]
    encrypted_text_length -= encrypted_key_length

print("Textul decriptat este:", decrypted_text)