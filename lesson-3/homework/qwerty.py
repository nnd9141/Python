1. Ro‘yxat yaratish va uchinchi mevaning nomini chop etish

fruits = ['olma', 'banan', 'nok', 'anjir', 'shaftoli']
print("Uchinchi meva:", fruits[2])

------------------------------------------------------

2. Ikki ro‘yxatni birlashtirish

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Birlashtirilgan ro'yxat:", combined)

------------------------------------------------------

3. Ro‘yxatdan birinchi, o‘rta va oxirgi elementlarni ajratib olish

# Berilgan ro‘yxatdan birinchi, o‘rta va oxirgi elementlarni olib, yangi ro‘yxatga joylang.
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print("Ajratilgan elementlar:", extracted)

------------------------------------------------------

4. Ro‘yxatni tuple ga aylantirish

# Sevimli 5 ta film nomidan ro‘yxat yarating va uni tuple ga aylantiring.
movies = ['Inception', 'Avatar', 'Titanic', 'Interstellar', 'Joker']
movies_tuple = tuple(movies)
print("Tuple:", movies_tuple)

------------------------------------------------------

5. Ro‘yxatda "Paris" borligini tekshirish

# Shaharlar ro‘yxatidan "Paris" bor-yo‘qligini tekshiring va natijani chop eting.
cities = ['Toshkent', 'London', 'Paris', 'New York']
if 'Paris' in cities:
    print("Ro'yxatda Paris bor.")
else:
    print("Ro'yxatda Paris yo'q.")


------------------------------------------------------

6. Ro‘yxatni siklsiz takrorlash

# Raqamlardan iborat ro‘yxatni sikl ishlatmasdan ikki marta takrorlang.
numbers = [1, 2, 3]
duplicated = numbers * 2
print("Takrorlangan ro'yxat:", duplicated)

------------------------------------------------------

7. Ro‘yxatdagi birinchi va oxirgi elementlarni almashtirish

# Ro‘yxatdagi birinchi va oxirgi elementlarning joyini almashtiring.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("Almashtirilgan ro'yxat:", numbers)

------------------------------------------------------

8. Tuple dan kesma olish
# 1 dan 10 gacha sonlardan tuple yaratib, 3-dan 7-gacha indekslar oralig‘ini chop eting.
numbers = tuple(range(1, 11))
slice_part = numbers[3:8]
print("Kesilgan tuple:", slice_part)

------------------------------------------------------

9. Ro‘yxatda "blue" necha marta uchraganini sanash

# Ranglar ro‘yxatida "blue" necha marta borligini hisoblang.
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
count_blue = colors.count('blue')
print("Blue rangi soni:", count_blue)

------------------------------------------------------

10. Tuple da "lion" indeksini topish
# Hayvonlar tuple dan "lion" ning indeksini toping.
animals = ('cat', 'dog', 'lion', 'tiger')
index_lion = animals.index('lion')
print("Lion indeksi:", index_lion)

------------------------------------------------------

11. Ikki tuple ni birlashtirish

# Ikki tuple ni bitta tuple ga birlashtiring.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print("Birlashtirilgan tuple:", merged)

------------------------------------------------------

12. Ro‘yxat va tuple uzunligini topish

# Berilgan ro‘yxat va tuple uzunligini toping va chop eting.
lst = [1, 2, 3, 4]
tpl = (5, 6, 7)
print("Ro'yxat uzunligi:", len(lst))
print("Tuple uzunligi:", len(tpl))

------------------------------------------------------

13. Tuple ni ro‘yxatga aylantirish

# 5 ta sondan iborat tuple ni ro‘yxatga aylantiring.
tpl = (10, 20, 30, 40, 50)
lst = list(tpl)
print("Ro'yxat:", lst)

------------------------------------------------------

14. Tuple dan eng katta va eng kichik qiymatlarni topish

# Tuple dan eng katta va eng kichik qiymatlarni toping.
numbers = (5, 3, 9, 1, 7)
print("Eng katta:", max(numbers))
print("Eng kichik:", min(numbers))

------------------------------------------------------

15. Tuple ni teskari tartibda chiqarish

# So‘zlardan iborat tuple ni teskari tartibda chop eting.
words = ('salom', 'dunyo', 'python', 'kod')
reversed_words = words[::-1]
print("Teskari tartibda:", reversed_words)














































    
