while True:
    yosh = int(input("Yoshingizni kiriting (Dastur toxtashi uchun 0 kiriting): "))
    
    if yosh == 0:
        print("dastur tugadi.")
        break
    elif yosh < 18:
        print("hali kichkina ekansiz.")
    else:
        print("Xush kelibsiz.")


kitoblar = []

while True:
    kitob = input("Sevimli kitobingizni kiriting: ")
    
    if kitob.lower() == "stop":
        break
    kitoblar.append(kitob)
print("kiritilgan kitoblar:")
for kitob in kitoblar:
    print(kitob)


# import random 
# tasodifiy_son = random.randint(1,10)
# while True:
#     try:
#         taxmin = int(input("1 dan 10gacha bolgan sonni kiriting "))
#         if taxmin == tasodifiy_son:
#             print("Tabriklaymiz togri topdingiz")
#             break
#         else:
#             print("Xato")
#     except ValueError:
#         print("Iltimos faqat butun son kiriting")        