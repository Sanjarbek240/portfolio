from a import mahsulotlar

narxlar = []
while True:
    nom = input("Mahsulot nomini kiriting: ").lower()
    if nom in mahsulotlar:
        narx = mahsulotlar[nom]
        narxlar.append(narx)
        print(f"{nom.title()} narxi {narx} so'm.")
    else:
        print("Kechirasiz, bu mahsulot mavjud emas.")
    
    davom_et = input("Yana mahsulot tanlaysizmi? (ha/yo'q): ").lower()
    if davom_et != "ha":
        break

jami = sum(narxlar)
print(f"\nSiz uchun to'lov miqdori: {jami} so'm.")
