ismlar = []
while True:
    ism = input("Ismingizni kiriting (toxtatish uchun 'stop' deb yozing): ")
    
    if ism.lower() == "stop": 
        break
    
    ismlar.append(ism)  

print("\nKiritilgan ismlar royxati:")
for ism in ismlar:
    print(ism)
