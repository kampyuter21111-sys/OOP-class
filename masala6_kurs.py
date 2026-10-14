class Kurs:
    def __init__(self, nomi, davomiylik):
        self.nomi = nomi
        self.davomiylik = davomiylik
        self.talabalar = []   
    def talaba_qoshish(self, ism):
        self.talabalar.append(ism)

    def talabalar_soni(self):
        return len(self.talabalar)


kurs = Kurs("Python", "3 oy")
kurs.talaba_qoshish("Ali")
kurs.talaba_qoshish("Vali")
kurs.talaba_qoshish("Gulnora")
print("Talabalar soni:", kurs.talabalar_soni())
