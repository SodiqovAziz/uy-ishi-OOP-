import time
from datetime import datetime
class Odam:
    def __init__(self,ism):
        self.ism=ism
        k=0
        e=0
    def yugurish(self):
        self.k=1
    def yiqilish(self):
        self.e=1
        if self.k==1:
            print("Yugurishni boshladi")
            start_time=datetime.now
            time.sleep(5)
            e=1
            print("Yiqildi")
x=input("Ismini kiriting: ")
odam=Odam(x)
odam.yugurish()
odam.yiqilish()
