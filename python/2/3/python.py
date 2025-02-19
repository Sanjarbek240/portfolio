# menu = ['osh','somsa','shorva','lavash'] or ['osh ','somsa ','shorva ','lavash '] 
# buyurtmalar = []
# narx = 0
# x = int(input("Hurmatli mijoz siz nechta taom buyurma qilasiz:\t"))
# for i in range(0,x):
#     buyurtma = input(f"{i+1}buyurma kiriting:\t")
#     buyurtmalar.append(buyurtma)

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"sizning {taom.title()} nomli buyurtmangiz qabul qilindi")
#         else:
#             print(f"sizning{taom.title()}nomli buyurtmangiz mavjud emas!")
# else:
#     print("Savatchangiz bosh")
# print(f"\nSizning buyurmalar soningiz: {len(buyurtmalar)}")

# for a in buyurtmalar:
#   if a == 'osh':
#     narx += 10000
#   if a == 'somsa':
#     narx +=a
#   if a == 'shorva':
#     narx += 20000
#   if a == 'lavash':
#     narx += 25000

# print(f"sizning tolovingiz: {narx}")



# yosh = int(input("yoshingizni kiriting:"))

# if yosh < 18:
#     print("sizga kirish taqiqlanadi")
# elif yosh >= 18:
#     print("Xush kelibsiz")    


kun = input("Hafta kunini kiriting: ")
kun.lower()

if kun == "shanba" or kun == "yakshanba":
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")