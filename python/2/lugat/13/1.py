# a = {"first": "developer", "second": "pythonista", "third": "coder"}

# b = list(a.values())[0]
# for c in a.values():
#     if len(c) > len(b):
#         b = c

# print("uzuni:", b)



# lugat = {"olma": 50, "banan": 20, "apelsin": 30}

# nomi = input("nomi:").lower()
# miqdori = int(input("miqdori: "))

# if nomi in lugat and lugat[nomi] >= miqdori:
#     lugat[nomi] -= miqdori
#     print(f"{miqdori} dona {nomi} sotildi-qolgani: {lugat[nomi]}")
# else:
#     print("tugagan!")

# a = input("soz kiriting: ")
# soni = {}

# for harf in a:
#     soni[harf] = soni.get(harf, 0) + 1

# print(soni)

# a = {'a': 3, 'b': 8, 'c': 1, 'd': 6, 'e': 2}

# b = list(a.items()) 
# n = len(b)

# for i in range(n):
#     for d in range(n - 1):
#         if b[d][1] > b[d + 1][1]:  
#             b[d], b[d + 1] = b[d + 1], b[j]  

# lugat = {}
# for kalit, qiymat in b:
#     lugat[kalit] = qiymat

# print("tartiblangan:", lugat)





kontaklar = {
    'husan' : 975216686,
    'sanjar': 948300425
}

tanlov = input("1 - Yangi Kontakt ,  2 - Kontakt qidirish")

if tanlov == '1':
    kontaklar[input("Ism kiriting")] = input("Telefon raqam kiriting")
    print("Kontakt qowildi")

if tanlov == 2:
    print(kontaklar.get(input("Qidirilgan ish"), "Bunday kontakt yoq"))    