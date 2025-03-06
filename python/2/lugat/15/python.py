# Bo‘sh ro‘yxat yaratamiz
ismlar = []

# Foydalanuvchidan ism kiritishni so‘raymiz
while True:
    ism = input("Ismingizni kiriting (to‘xtatish uchun 'stop' deb yozing): ")
    
    if ism.lower() == "stop":  # Agar "stop" deb yozsa, tsikl to‘xtaydi
        break
    
    ismlar.append(ism)  # Ismni ro‘yxatga qo‘shamiz

# Yakuniy ro‘yxatni chiqaramiz
print("\nKiritilgan ismlar ro‘yxati:")
for ism in ismlar:
    print(ism)
