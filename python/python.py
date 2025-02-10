ism = input("ismingiz nima?\t >>>")
if ism.lower() != 'sanjar':
    print(f"Uzr, {ism.title()} biz Sanjarni kutyabmiz")
else:
    print("Salom,Sanjar")    


javob = float(input("12*6 nechiga teng"))
if javob != 72:
    print("javob xato")
else:
    print("javob togri")    

yosh = int(input("Yoshingiz nechidaa?>>>"))
if yosh >= 18:
    print('Xush kelibsiz')
else:
    print('Kirish mumkin emas')    



login = input("Yangi login tanlang")
if len(login)<=5:
    print("login 5harfdan koproq bolishi krak")
else:
    print(f"{login} login sifatida qabul qilindi")   7


yosh = int(input("Yoshingizni kiriting:"))
if yosh < 18:
    print("Siz {yosh}yoshda ekansiz sizga kirish bepul")
elif 18 <= yosh <= 35:
    print("Siz {yosh}yoshda ekansiz sizga kirish narxi 10000som")
    
else:
    print("Siz {yosh}yoshda ekansiz kirish narxi 5000som ")



a = int(input("1-soni kiriting:"))
b = int(input("2-soni kiriting:"))
d = int(input("3-soni kiriting:"))

son = [a,b,d]
son.sort()
print(son)

login = input("Loginingizni kiriting")
parol = input("Parolingizni kiriting")

if login.lower() =="admin" and parol=="12345":
    print("Xush kelibsiz")
else:
    print("Login yoki parol xato")    