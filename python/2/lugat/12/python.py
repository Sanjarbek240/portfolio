# a = {
#     "til" : ["Python","CSS","HTML"] 
# }
# print("Men bilgan dasturlash tillari")
# for b in a["til"]:
#     print(f"  {b}")




# kitoblar = [
#     {"nomi": "UFQ", "muallif": "Otkir Hoshimov", "yili": 1984},
#     {"nomi": 1984, "muallif": "Jorj Oruell", "yili": 1949},
#     {"nomi": "Allkimyogar", "muallif": "Pauleo Kalyuelolo", "yili": 1988},
#     {"nomi": "Dunyo Ishlari", "muallif": "Otkir Hoshimov", "yili": 2011},
#     {"nomi": "Kecha va kunduz", "muallif": "Cholpon", "yili": 1936}
# ]


# print("Kitoblar ro'yxati:\n")
# for kitob in kitoblar:
#     print(f"Nomi: {kitob['nomi']}")
#     print(f"Muallif: {kitob['muallif']}")
#     print(f"Chop etilgan yili: {kitob['yili']}")


cars = [
    {"turi": "Malibu", "rang":"oq","narxi":"35000"},
    {"turi": "Spark", "rang":"qizil","narxi":"12000"},
    {"turi": "Cobalt", "rang":"qora","narxi":"14000"},
    {"turi": "BMW X8", "rang":"qora","narxi":"40000"},
    {"turi": "Nexia", "rang":"kok","narxi":"13000"}
    
]
for car in cars:
    if car['narx'] >30000:
        narx = 'qimmat'
    else:
        narx = 'azon' 

print(f"{car['model']} ({car['rang']} rangda) - {narx}")          