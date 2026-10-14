class Avtomobil:
    def __init__(self, model, yil, tezlik=0):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def tezlashtir(self):
        self.tezlik += 10

    def sekinlashtir(self):
        self.tezlik -= 10

    def info(self):
        print(f"Model: {self.model}, Yil: {self.yil}, Tezlik: {self.tezlik} km/s")


a = Avtomobil("Chevrolet Malibu", 2022)
a.tezlashtir()
a.tezlashtir()
a.tezlashtir()
a.sekinlashtir()
a.info()
