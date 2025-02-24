f = {
    "brand" : "ford",
    "electric" : False,
    "year" : 1964,
    "color" : ["white","black","red"]

}

for t,e in f.items():
    if t == "color":
        print(f"t")
        for rang in e:
            print(f"          -{rang}") 
    else:       
        print(f"{t}  {e}")