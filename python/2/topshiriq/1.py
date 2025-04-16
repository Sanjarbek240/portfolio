login = input("login kiriting ")
password = input("parol kiriting ")
a = "sanjar"
b = "karimov"

if login == a and password == b:
    isim = input("qaysi sanjar haqida malumot kerak? ")
    print(f"{isim} haqida malumot")

    c= input(" yana qaysi ismga malumot kerak?bolsa yana isim kiriting bolmasa(stop)deb yozing! ")
    if c.lower() == "stop":
        print("tugadi")
    else:
        c= input("isim kiriting ")
        print(f"{c} haqida malumo")
else:
    print("togri login parol kirting")