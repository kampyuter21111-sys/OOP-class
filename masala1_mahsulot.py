class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor

    def sotib_ol(self, miqdor):
        if miqdor <= self.miqdor:
            self.miqdor -= miqdor
            print(f"{miqdor} ta {self.nom} sotib olindi")
        else:
            print("Omborda yetarli mahsulot yo'q!")

    def qolgan_miqdor(self):
        return self.miqdor


m = Mahsulot("Olma", 12000, 50)
m.sotib_ol(10)
m.sotib_ol(5)
print("Qolgan miqdor:", m.qolgan_miqdor())
