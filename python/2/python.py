# foydalanuvchi = int(input("Bahoni kiriting:"))

# if foydalanuvchi >= 90:
#     print("A")
# elif foydalanuvchi >=80:
#     print("B")
# elif foydalanuvchi >= 70:
#     print("C")        
# elif foydalanuvchi >=60:
#     print("D")
# else:
#     print("F")        


# n = int(input("Ixtiyoriy son kiriting"))

# if n % 3 == 0 and n % 5 == 0:

#     print("FizzBuzz")
# elif n%5==0:
#     print("Buzz")
# elif n%3==0 :
#     print("Fizz")
# else:
#     print(n)           


a = input("matn kiriting")
unlilar = "AEUIOO'aeuioo'"
soni = 0

for matn in a:
    if matn in unlilar:
        soni+=1

print(soni)        
