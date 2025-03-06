# ismlar = []
# while True:
#     ism = input("Ismingizni kiriting (toxtatish uchun 'stop' deb yozing): ")
    
#     if ism.lower() == "stop": 
#         break
    
#     ismlar.append(ism)  

# print("\nKiritilgan ismlar royxati:")
# for ism in ismlar:
#     print(ism)

mevalar = ["olma", "banan", "olma", "shaftoli", "olma"]

# "olma" ro‘yxatda bor ekan, uni o‘chiramiz
while "olma" in mevalar:
    mevalar.remove("olma")

# Natijaviy ro‘yxatni chiqaramiz
print("Yangilangan ro‘yxat:", mevalar)
