class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def qidirish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nomi == nom:
                return kitob
        return None


kutubxona = Kutubxona()
kutubxona.kitob_qoshish(Kitob("O'tkan kunlar", "Abdulla Qodiriy"))
kutubxona.kitob_qoshish(Kitob("Mehrobdan chayon", "Abdulla Qodiriy"))
kutubxona.kitob_qoshish(Kitob("Sariq devni minib", "Xudoyberdi To'xtaboyev"))

topilgan = kutubxona.qidirish("Mehrobdan chayon")
if topilgan:
    print(f"Topildi: {topilgan.nomi} - {topilgan.muallif}")
else:
    print("Kitob topilmadi")
