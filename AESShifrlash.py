
#AES — bitta blok uchun
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
 
def aes_blok(kalit, blok16):          # faqat tajriba uchun
    shifr = Cipher(algorithms.AES(kalit), modes.ECB()).encryptor()
    return shifr.update(blok16) + shifr.finalize()
 
def farqli_bitlar(a, b):
    return sum(bin(x ^ y).count("1") for x, y in zip(a, b))
 
kalit = os.urandom(16)                  # tasodifiy 128 bitli kalit
b1 = b"KRIPTOGRAFIYA123"
b2 = b"KRIPTOGRAFIYA122"                # faqat oxirgi belgi farq qiladi
c1, c2 = aes_blok(kalit, b1), aes_blok(kalit, b2)
print("Kalit :", kalit.hex())
print("C1    :", c1.hex())
print("C2    :", c2.hex())
print("Ochiq matnlarda farqli bitlar:", farqli_bitlar(b1, b2))
print("Shifrmatnlarda farqli bitlar :", farqli_bitlar(c1, c2), "/ 128")
