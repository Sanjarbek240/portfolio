a = int(input("son kiriting: "))
b = [i for i in range(1, a) if a % i == 0]
if sum(b) == a:
    print("mukammal son")
else:
    print("mukammal son emas")
