Dictionary

---

1. Lug‘atni qiymat bo‘yicha tartiblash (oshish va kamayish tartibida)


# Berilgan lug‘atni qiymatlar bo‘yicha oshish va kamayish tartibida tartiblang.

my_dict = {'a': 3, 'b': 1, 'c': 2}

# Oshish tartibida
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Oshish tartibida:", asc_sorted)

# Kamayish tartibida
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Kamayish tartibida:", desc_sorted)


---

2. Lug‘atga yangi kalit qo‘shish


# Berilgan lug‘atga yangi kalit (key) va qiymat qo‘shing.
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Yangilangan lug‘at:", my_dict)


---

3. Bir nechta lug‘atlarni birlashtirish


# Uchta lug‘atni bitta yangi lug‘atga birlashtiring.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = {}
for d in (dic1, dic2, dic3):
    merged.update(d)

print("Birlashtirilgan lug‘at:", merged)


---

4. 1 dan n gacha bo‘lgan sonlar kvadratidan lug‘at yaratish


# 1 dan n gacha bo‘lgan sonlar uchun (x: x*x) ko‘rinishida lug‘at yarating.

n = 5
squares = {x: x**2 for x in range(1, n+1)}
print("Kvadratli lug‘at:", squares)


---

5. 1 dan 15 gacha bo‘lgan sonlar kvadratlari lug‘atini chop etish


# Kalitlar 1 dan 15 gacha, qiymatlar ularning kvadrati bo‘lgan lug‘atni chop eting.

squares = {x: x**2 for x in range(1, 16)}
print("1 dan 15 gacha kvadratlar lug‘ati:", squares)


---

Set 

---

1. Set yaratish


# Python dasturi orqali oddiy set yarating.
my_set = {1, 2, 3, 4}
print("Yaratilgan set:", my_set)


---

2. Set elementlarini aylanish (iterate) orqali chiqarish


# Set ichidagi barcha elementlarni birma-bir chop eting.
my_set = {'apple', 'banana', 'cherry'}
for item in my_set:
    print(item)


---

3. Setga element qo‘shish


# Setga bitta yoki bir nechta element qo‘shing.
my_set = {1, 2, 3}
my_set.add(4)  
my_set.update([5, 6])
print("Yangilangan set:", my_set)


---

4. Setdan element(lar)ni o‘chirish


# Setdan elementlarni o‘chiring.
my_set = {1, 2, 3, 4}
my_set.remove(3)  
# my_set.remove(10)
print("O‘chirilgan set:", my_set)


---

5. Agar mavjud bo‘lsa, elementni setdan o‘chirish


# Agar element mavjud bo‘lsa, uni setdan o‘chiring (xatolik bo‘lmasin).

my_set = {1, 2, 3, 4}
my_set.discard(3)  
my_set.discard(10)  
print("Set:", my_set)



