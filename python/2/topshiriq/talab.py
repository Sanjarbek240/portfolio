class Talab:
   def __init__(self,ism,familya,kurs,yonalissh,tugulgan_yilii):
      self.ism =ism
      self.familya = familya
      self.kurs=kurs
      self.yonalissh=yonalissh
      self.tugulgan_yilii= tugulgan_yilii
   def malumot(self):
       return{
          "isim" :self.ism,
          "familya":self.familya,
          "kurs": self.kurs,
          "yonalish":self.yonalissh,
          "tuhulgan":self.tugulgan_yilii
       }
   def kunga(self,tugulgan_kun):
      from datetime import datetime
      tugulgan_kun = datetime.strptime(tugulgan_kun, "%Y-%m-%d")
      return (tugulgan_kun - datetime.now()).days