class Odam:
    def __init__(self, ism):
        self.ism = ism
        self.k = 0
        self.e = 0
    def kuylash(self):
        self.k = 1
    def eshitish(self):
        self.e = 1
    def gapirish(self):
        if self.k==1:
            print('Kuylandi')
        else:
            print('Kuylanmadi')
        if self.e == 1:
            print('Eshitildi')
        else:
            print('Eshitilmadi')
        if self.k==1 and self.e==1:
            print('Gapirish mumkin')
        else:
            print('Ukam gapirishni iloji yo`q')
x = input('Ismini kiriting: ')
odam = Odam(x)
odam.kuylash()
odam.gapirish()
