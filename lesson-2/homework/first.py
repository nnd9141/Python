Age Calculator

a = input('Ismingizni kiriting')
b = int(input('Tugilgan yilingizni kiriting !'))

c = 2025 - b

print(a, c)

-------------------------------------------------

Extract Car Names

txt = 'LMaasleitbtui'

a = txt[::2]

b = txt[1::2]

print(a,b)

-------------------------------------------------

Extract Car Names

txt = 'MsaatmiazD'

a = txt[::2]

b = txt[::-2]

print(a,b)

-------------------------------------------------

Extract Residence Area

txt = "I'am John. I am from London"

a = txt[21:27]

print(a)

-------------------------------------------------

txt = input("Matn kiriting: ")

a = txt[::-1]

print(a)

-------------------------------------------------

Count Vowels

text = input("Matn kiriting: ").lower()
vowels = 'aeiou'
count = sum(1 for char in text if char in vowels)
print("Unli harflar soni:", count)

-------------------------------------------------

sonlar = [3, 5, 2, 8, 1]

eng_katta = max(sonlar)

print(eng_katta) 

-------------------------------------------------

Check Palindrome

soz = input("So'z kiriting: ").lower()

teskari = soz_tahlil[::-1]

if soz_tahlil == teskari:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")

-------------------------------------------------

Extract Email Domain

email = input("Email manzilini kiriting: ")

if '@' in email:
    domen = email.split('.')[1]
    print("Domen qismi:", domen)
else:
    print("Email manzilda '@' belgisi yo'q. Iltimos, to‘g‘ri email kiriting.")

-------------------------------------------------

Generate Random Password

import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))
belgilar = string.ascii_letters + string.digits + string.punctuation
parol = ''.join(random.choice(belgilar) for _ in range(uzunlik))

print("Yaratilgan parol:", parol)
