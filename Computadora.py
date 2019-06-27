from CPU import CPU
from Memoria import Memory
from Puertos import Puertos
from Screen import Screen
import pygame
class Computer:
    def __init__(self, rom="invaders.rom"):
        self.cpu = CPU()
        self.memory = Memory()
        self.memory.Load(rom)
        self.ports = Puertos()
        self.Screen = Screen()

    def execute(self):
        instructions_per_frame=10
        while not self.cpu.getStatus():
            for i in range(instructions_per_frame):
                self.Prompt()
            #screenDisplay
            self.Screen.display(self.memory)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 274:
                        pygame.quit()

    def Prompt(self):
        self.cpu.getALU().displayFlags()
        self.cpu.getRegisters().displayRegisters()
        print("PC =", hex(self.cpu.getPC()))
        print("SP =", hex(self.cpu.getSP()))
        instruction = input(">").upper()
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
            self.memory.getMemory(addr)
            value = int(input("Valor="))
            self.memory.setMemory(addr, value)
        elif instruction == "W":
            filename = input("Nombre del archivo")
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
    
    pygame.init()
    c = Computer()
    #for i in c.memory.Memory[0x2400:0x3fff]:
    #    print(hex(i), end=" ")

    c.execute()
