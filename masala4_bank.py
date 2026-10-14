class BankHisob:
    def __init__(self, ism, balans=0):
        self.ism = ism
        self.balans = balans

    def deposit(self, summa):
        self.balans += summa

    def yechib_ol(self, summa):
        if summa <= self.balans:
            self.balans -= summa
        else:
            print("Hisobda yetarli mablag' yo'q!")

    def hisob(self):
        return self.balans


h = BankHisob("Ali")
h.deposit(1000)
h.yechib_ol(400)
print(f"{h.ism}ning balansi:", h.hisob())
