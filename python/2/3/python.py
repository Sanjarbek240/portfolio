menu = ['osh','somsa','shorva','lavash']
buyurtmalar = []
narx = 0
x = int(input("Hurmatli mijoz siz nechta taom buyurma qilasiz:\t"))
for i in range(0,x):
    buyurtma = input(f"{i+1}buyurma kiriting:\t")
    buyurtmalar.append(buyurtma)

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"sizning {taom.title()} nomli buyurtmangiz qabul qilindi")
        else:
            print(f"sizning{taom.title()}nomli buyurtmangiz mavjud emas!")
else:
    print("Savatchangiz bosh")
print(f"\nSizning buyurmalar soningiz: {len(buyurtmalar)}")

if buyurtma == 'osh':
    narx += 10000
if buyurtma == 'somsa':
    narx+=15000
if buyurtma == 'shorva':
    narx += 20000
if buyurtma == 'lavash':
    narx += 25000

print(f"sizning tolovingiz: {narx}")


