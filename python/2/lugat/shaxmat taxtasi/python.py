# Shaxmat taxtasida harakatlanayotgan ot ning yurish yo‘lini topadigan dastur yozing. Dastur:
# ✅ 8x8 taxta yaratishi kerak.
# ✅ Otni boshlang‘ich nuqtaga qo‘yishi kerak.
# ✅ Barcha yurishlarni topish uchun rekursiv algoritm ishlatishi kerak.
# ✅ While, for va def dan foydalanib, kodni to‘liq bajarishi kerak.


# def shaxmat():
#     for i in range(8):
#         for j in range(8):
#             if (i + j) % 2 == 0:
#                 print("⬜", end=" ") 
#             else:
#                 print("⬛", end=" ")  
#         print()

# shaxmat()


def shaxmat_taxtasi():
    taxta = [[0 for _ in range(8)] for _ in range(8)]
    return taxta

def ot_harakatlari(x, y, taxta):
    if x < 0 or x >= 8 or y < 0 or y >= 8 or taxta[x][y] != 0:
        return
    taxta[x][y] = 1  # Ot joylashgan joy
    for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
        ot_harakatlari(x + dx, y + dy, taxta)
    taxta[x][y] = 0  # Orqaga qaytishi

# Asosiy funksiya
def asosiy_funksiya():
    taxta = shaxmat_taxtasi()
    boshlangich_x, boshlangich_y = 0, 0  # Yuqoridan chapga
    ot_harakatlari(boshlangich_x, boshlangich_y, taxta)
    for qator in taxta:
        print(" ".join(str(x) for x in qator))

asosiy_funksiya()

