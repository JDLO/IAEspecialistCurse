class Coche:    
    def __init__(self, brand='', power=0, isStart=False):
        super().__init__()
        self.brand = brand
        self.power = power
        self.isStart = isStart

    def arrancar(self):
        self.isStart = True
        print("Esta arrancado el coche")

    def parar(self):
        self.isStart = False
        print("Esta apagado el coche")

    def estadoActual(self):
        return f"el estado actual del coche es: {'arrancado' if self.isStart else 'apagado'}"

    def __str__(self):
        return f"El coche es un {self.brand} de potencia {self.power} CV y {self.estadoActual()}"
    def claxon(self, duration=1):
        print("P" + "i"*duration + "!")

class Limousine(Coche):
    def __init__(self, brand, power, isStart=False, capacityMiniBar=0):
        super().__init__(brand, power, isStart)
        self.miniBarCapacity = capacityMiniBar
    def __str__(self):
        return super().__str__() + f", ademas su capacidad del mini bar es de: {self.miniBarCapacity}L"
    def claxon(self, duration=1):
        print("P" + "o"*duration + "m!")
         

cocheByd = Coche('BYD', 150, False)
coche01 = Coche('Toyota', 150)
coche02 = Coche('Ford', 150, True)
limosina = Limousine('Lincoln', 300, capacityMiniBar=60)

cocheByd.arrancar()
coche01.arrancar()
coche02.parar()

listCoches = [cocheByd, coche01, coche02, limosina]

for coche in listCoches:
    print(coche)
    coche.claxon(5)
    if coche.isStart:
        coche.isStart = False
    else:
        coche.isStart = True

for coche in listCoches:
    print(coche)