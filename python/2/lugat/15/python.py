# ismlar = []
# while True:
#     ism = input("Ismingizni kiriting (toxtatish uchun 'stop' deb yozing): ")
    
#     if ism.lower() == "stop": 
#         break
    
#     ismlar.append(ism)  

# print("\nKiritilgan ismlar royxati:")
# for ism in ismlar:
#     print(ism)

# mevalar = ["olma", "banan", "olma", "shaftoli", "olma"]

# while "olma" in mevalar:
#     mevalar.remove("olma")
# print(mevalar)

talabalar = ["Ali","Vali","Hasan"]
n = 0
baholar = {}

while n < len(talabalar):
    talaba = talabalar[n]
    n = 1+n
    ball = int(input(f"{talaba}ning bahosini kiriting:"))
    baholar[talaba] = ball
print("\n Talabalar baxosi")
for i,b in baholar.items():
    print(f"{i}ning bahosi {b}")