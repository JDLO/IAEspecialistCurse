class Mesa:
    numPatas: int
    color: str

    def __init__(self, numPatas=1, color='white'):
        self.numPatas = numPatas
        self.color = color
    def __str__(self):
        return f"La mesa tiene " + str(self.numPatas) + " patas y es de color " + self.color 

mesa = Mesa()
print(mesa)