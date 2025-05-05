class oquvchi:
    def __init__(self,isim):
        self.isim = isim
        self.baho = []
    def baholar(self,bahosi):
        if 1<= bahosi<= 5:
            self.baho.append(bahosi)
        else:
            raise ValueError("1dan beshgacha bolishi kerak baho")
    def baholar_olish(self):
        return self.baho.copy()            
   
o1 = oquvchi("Sanjar")
o1.baholar(3)
print(o1.baholar_olish())

o2 = oquvchi("aziz")
o2.baholar(5)
print(o2.baholar_olish)
