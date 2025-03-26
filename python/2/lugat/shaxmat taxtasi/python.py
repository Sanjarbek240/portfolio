# Shaxmat taxtasida harakatlanayotgan ot ning yurish yo‘lini topadigan dastur yozing. Dastur:
# ✅ 8x8 taxta yaratishi kerak.
# ✅ Otni boshlang‘ich nuqtaga qo‘yishi kerak.
# ✅ Barcha yurishlarni topish uchun rekursiv algoritm ishlatishi kerak.
# ✅ While, for va def dan foydalanib, kodni to‘liq bajarishi kerak.


def shaxmat():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                print("⬜", end=" ") 
            else:
                print("⬛", end=" ")  
        print()

shaxmat()