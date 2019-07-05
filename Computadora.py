import sys;
from CPU import CPU
from Memoria import Memory
from Puertos import Puertos
from Screen import Screen
class Computer:
    def __init__(self, rom="invaders.rom"):
        self.cpu = CPU()
        self.memory = Memory()
        self.memory.Load(rom)

        self.ports = Puertos()
        self.Screen = Screen()
    #push rrc ani call pop ret incx lxi
    def execute(self):
        instructions_per_frame=1000
        while not self.cpu.getStatus():
            i=0
            while i < instructions_per_frame and not self.cpu.getStatus():
                self.Prompt()
                i += 1
            #screenDisplay
            self.Screen.display(self.memory)
            #input()
            

    def Prompt(self):
        self.cpu.getALU().displayFlags()
        self.cpu.getRegisters().displayRegisters()
        print("PC =", hex(self.cpu.getPC()))
        print("SP =", hex(self.cpu.getSP()))
        instruction = 0 #input(">").upper()
        if instruction == "Q":
            self.cpu.setStatus(True)  # halt
        elif instruction == "A":
            value = int(input("A="))
            self.cpu.setRegister("A", value)
        elif instruction == "B":
            value = int(input("B="))
            self.cpu.setRegister("B", value)
        elif instruction == "C":
            value = int(input("C="))
            self.cpu.setRegister("C", value)
        elif instruction == "D":
            value = int(input("D="))
            self.cpu.setRegister("D", value)
        elif instruction == "E":
            value = int(input("E="))
            self.cpu.setRegister("E", value)
        elif instruction == "H":
            value = int(input("H="))
            self.cpu.setRegister("H", value)
        elif instruction == "L":
            value = int(input("L="))
            self.cpu.setRegister("L", value)
        elif instruction == "P":
            value = int(input("PC="))
            self.cpu.setPC(value,self.memory)
        elif instruction == "S":
            value = int(input("SP="))
            self.cpu.setSP(value,self.memory)
        elif instruction == "M":
            addr = int(input("Dir="))
            value = int(input("Valor="))
           
            self.memory.setMemory(addr, value)
        elif instruction == "W":
            filename = input("Nombre del archivo: ")
            self.memory.Write(filename)
        else:
            self.cpu.execute(self.memory, self.ports)

        # Check if interruption


'''
a 127
m
d 0
v 23
'''
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("I need rom file")
    else:
        c = Computer(sys.argv[1])
        c.execute()
