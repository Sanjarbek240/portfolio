# f = {
#     "brand" : "ford",
#     "electric" : False,
#     "year" : 1964,
#     "color" : ["white","black","red"]

# }

# for t,e in f.items():
#     if t == "color":
#         print(f"t")
#         for rang in e:
#             print(f"          -{rang}") 
#     else:       
#         print(f"{t}  {e}")


#1

# kitoblar = {
#         "Python" : "Guido van Rossum",
#         "Java" : "James Gosling",
#         "C++" : "Bjarne Stroustrup"
# }

# print(f"{kitoblar}")


#2

# bollar = {
#     "Ali": 85, 
#     "Vali": 92, 
#     "Hasan": 78, 
#     "Gani": 99
# }
# kattasi = None

# for ball in bollar.values():
#     print(f"{ball}")
#     if kattasi is None or ball > kattasi:
#         kattasi = ball


# print(f"Eng kattasi: {kattasi}")   


# 3 
talabalar = {
    "Ali": {"yosh": 20, "kurs": 2, "universitet": "TATU"},
    "Vali": {"yosh": 21, "kurs": 3, "universitet": "SAMDU"}
}

print(f"Ali universiteti - {talabalar['Ali']['universitet']}")       

talabalar['Vali']['kurs'] = 4   
print(talabalar)