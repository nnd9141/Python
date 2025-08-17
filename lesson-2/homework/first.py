a = input('Ismingizni kiriting')
b = int(input('Tugilgan yilingizni kiriting !'))

c = 2025 - b

print(a, c)

-------------------------------------------------

txt = 'LMaasleitbtui'

a = txt[::2]

b = txt[1::2]

print(a,b)

-------------------------------------------------

txt = 'MsaatmiazD'

a = txt[::2]

b = txt[::-2]

print(a,b)

-------------------------------------------------

txt = "I'am John. I am from London"

a = txt[21:27]

print(a)

-------------------------------------------------

txt = 'Salom'

a = txt[::-1]

print(a)

-------------------------------------------------

-------------------------------------------------

sonlar = [3, 5, 2, 8, 1]

eng_katta = max(sonlar)

print(eng_katta) 

-------------------------------------------------

soz = input("So'z kiriting: ")

teskari = soz_tahlil[::-1]

if soz_tahlil == teskari:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")

-------------------------------------------------

email = input("Email manzilini kiriting: ")

if '@' in email:
    domen = email.split('.')[1]
    print("Domen qismi:", domen)
else:
    print("Email manzilda '@' belgisi yo'q. Iltimos, to‘g‘ri email kiriting.")

-------------------------------------------------

