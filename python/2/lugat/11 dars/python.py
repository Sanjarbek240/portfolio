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

bollar = {
    "Ali": 85, 
    "Vali": 92, 
    "Hasan": 78, 
    "Gani": 99
}
a = None

for b in bollar.items():
    print(f"{b}")
    if a is None or b > a:
        a = b
print(a)    