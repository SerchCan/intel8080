from CPU import CPU
from Memoria import Memory


class Computer:
    def __init__(self, rom="invaders.rom"):
        self.cpu = CPU()
        self.memory = Memory()
        self.memory.Load(rom)
        # self.memory.Write("file.txt")

    def execute(self):
        while not self.cpu.getStatus():
            self.Prompt()

    def Prompt(self):
        self.cpu.getALU().displayFlags()
        self.cpu.getRegisters().displayRegisters()
        print("PC =", hex(self.cpu.getPC().getValue()))
        print("SP =", hex(self.cpu.getSP().getValue()))
        instruction=input(">").upper()
        if instruction == "Q":
            self.cpu.setStatus(True)  # halt
        elif instruction == "A":
            value=int(input("A="))
            self.cpu.setRegisters("A", value)
        elif instruction == "B":
            value=int(input("B="))
            self.cpu.setRegisters("B", value)
        elif instruction == "C":
            value=int(input("C="))
            self.cpu.setRegisters("C", value)
        elif instruction == "D":
            value=int(input("D="))
            self.cpu.setRegisters("D", value)
        elif instruction == "E":
            value=int(input("E="))
            self.cpu.setRegisters("E", value)
        elif instruction == "H":
            value=int(input("H="))
            self.cpu.setRegisters("H", value)
        elif instruction == "L":
            value=int(input("L="))
            self.cpu.setRegisters("L", value)
        elif instruction == "P":
            value=int(input("PC="))
            self.cpu.setPC(value)
        elif instruction == "S":
            value=int(input("SP="))
            self.cpu.setSP(value)
        elif instruction == "M":
            addr=int(input("Dir="))
            self.memory.getMemory(addr)
            value=int(input("Valor="))
            self.memory.setMemory(addr, value)
        elif instruction == "W":
            filename=input("Nombre del archivo")
            self.memory.Write(filename)
        else:
            self.cpu.execute(self.memory)


if __name__ == "__main__":
    c=Computer()
    c.execute()
