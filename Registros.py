from Registro import Registro


class Registros:
    def __init__(self):
        self.Indexes = ["A", "B", "C", "D", "E", "H", "L"]
        self.Registers = {}
        for index in self.Indexes:
            self.Registers[index] = Registro()

    def setRegister(self, index, value):
        self.Registers[index.upper()].setValue(value)

    def getRegister(self, index):
        return self.Registers[index.upper()].getValue()

    def displayRegisters(self):
        endlers = ["\n", " : "]
        for i, index in enumerate(self.Indexes):
            print(index, "=", hex(self.getRegister(index)), end=endlers[i % 2])


if __name__ == "__main__":
    R = Registros()
    R.setRegister("A", 4)
    R.setRegister("C", 23)
    R.setRegister("L", 10)
    R.displayRegisters()
