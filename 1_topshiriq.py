class Odam():
    def __init__(self,ism):
        self.ism = ism
    def salomlashish(self):
        print(f"Salom {self.ism}")

ism_input = input('>>> ')
talaba1 = Odam(ism_input)
talaba1.salomlashish()
