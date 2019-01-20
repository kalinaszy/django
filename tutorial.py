names=["patrycja", "kasia", "aleksandra", "kalina"]
def sayhello(name):
    if len(name)==4:
        print("cześć ", name)
    else:
        print("hej")
def nazwa_funkcji():
    print("hej!!!")
for name in names:
    sayhello(name)


class Vehicle:
    def __init__(self, kolorkaroserii, liczbakol):
        self.kolorkaroserii=kolorkaroserii
        self.liczbakol=liczbakol
class Car(Vehicle):
    def __init__(self, kolorkaroserii):
        super().__init__(kolorkaroserii, 4)

mycar=Car("blue")
print(mycar.liczbakol)
