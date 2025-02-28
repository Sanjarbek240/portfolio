# a = {"first": "developer", "second": "pythonista", "third": "coder"}

# b = list(a.values())[0]
# for c in a.values():
#     if len(c) > len(b):
#         b = c

# print("uzuni:", b)



lugat = {"olma": 50, "banan": 20, "apelsin": 30}

nomi = input("Mahsulot nomi: ").lower()
miqdori = int(input("Miqdor: "))

if nomi in lugat and lugat[nomi] >= miqdori:
    lugat[nomi] -= miqdori
    print(f"{lugat} dona {nomi} sotildi. Qoldiq: {lugat[nomi]}")
else:
    print("Yetarli mahsulot yo‘q!")