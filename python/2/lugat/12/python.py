# a = {
#     "til" : ["Python","CSS","HTML"] 
# }
# print("Men bilgan dasturlash tillari")
# for b in a["til"]:
#     print(f"  {b}")




kitoblar = [
    {"nomi": "UFQ", "muallif": "Otkir Hoshimov", "yili": 1984},
    {"nomi": 1984, "muallif": "Jorj Oruell", "yili": 1949},
    {"nomi": "Allkimyogar", "muallif": "Pauleo Kalyuelolo", "yili": 1988},
    {"nomi": "Dunyo Ishlari", "muallif": "J.K. Rowling", "yili": 2011},
    {"nomi": "Don Kixot", "muallif": "Miguel de Cervantes", "yili": 1605}
]


print("Kitoblar ro'yxati:\n")
for kitob in kitoblar:
    print(f"Nomi: {kitob['nomi']}")
    print(f"Muallif: {kitob['muallif']}")
    print(f"Chop etilgan yili: {kitob['yili']}")