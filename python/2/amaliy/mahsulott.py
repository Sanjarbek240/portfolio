from mahsulot import mahsulotlar

narxlar = []
while True:
    nomi = input("mahsulot nomini belgilng: ").lower()
    if nomi in mahsulotlar:
        narx = mahsulotlar[nomi]
        narxlar.append(narx)
        print(f"{nomi.title()} narxi {narx} som.")
    else:
        print("mavjud emas.")
    
    b = input("yana mahsulot kerakmi").lower()
    if b != "ha":
        break

jami = sum(narxlar)
print(f"\ntolov miqdori: {jami} som.")