# a = int(input("son kiriting: "))
# b = [i for i in range(1, a) if a % i == 0]
# if sum(b) == a:
#     print("mukammal son")
# else:
#     print("mukammal son emas")


while True:
    try:
        a = int(input("son kiriting:"))
        if a % 2 == 0:
            print("Bu son juft son")
        else:
            print("Bu son toq")
            break
    except ValueError:
        print("butun son kiriiting")        