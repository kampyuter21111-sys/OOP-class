class Kitob:
    def __init__(self, nomi, muallif, sahifa_soni):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def qisqacha(self):
        return f"{self.nomi} - {self.muallif}, {self.sahifa_soni} sahifa"

    def katta_kitobmi(self):
        return self.sahifa_soni > 300


k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 400)
k2 = Kitob("Kichik shahzoda", "Antuan de Sent-Ekzyuperi", 120)

print(k1.qisqacha())
print("Katta kitobmi?", k1.katta_kitobmi())
print(k2.qisqacha())
print("Katta kitobmi?", k2.katta_kitobmi())
