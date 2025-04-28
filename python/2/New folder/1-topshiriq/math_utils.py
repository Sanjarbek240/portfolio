import main
a = float(input("1-son kiriting"))
b = float(input("2-son kiriting"))
c = input("+,-,*,/")
if c=='+':
    javob =main.add(a,b)
elif c =='-':
    javob= main.subtracta(a,b)        
elif c =='*':
    javob= main.multiply(a,b)  
elif c =='/':
    javob= main.divide(a,b)
else:
    print("xatoo")   

print(javob)             