from Registros import Registros
from Registro import Registro
from ALU import ALU
from Memoria import Memory


class CPU:
    def __init__(self):
        self.ALU = ALU()
        self.PC = Registro()
        self.SP = Registro(0xff)
        self.REGISTERS = Registros()
        self.halt = False
        self.I = 0
        self.Indexes = ["B", "C", "D", "E", "H", "L", "M", "A"]

    def getStatus(self):
        return self.halt

    def setStatus(self, halt):
        self.halt = halt

    def getALU(self):
        return self.ALU

    def getPC(self):
        return self.PC

    def getSP(self):
        return self.SP

    def getRegister(self,index):
        return self.REGISTERS.getRegister(index)

    def getRegisters(self):
        return self.REGISTERS
    def setRegister(self, index, value):
        self.REGISTERS.setRegister(index, value)

    def setPC(self, value):
        self.PC.setValue(value)

    def setSP(self, value):
        self.SP.setValue(value)

    def plusOnePC(self,Mem):
        self.PC.setValue( (self.PC.getValue()+1)%Mem.getSize())

    def execute(self, Mem):
        pc = self.PC.getValue()
        self.I = Mem.getMemory(pc)

        I = self.I
        if I == 0x00:
            print("no op")  # No Operation
        elif I == 0x07:
            self.RLC()
        elif I == 0x0f:
            self.RRC()
        elif I == 0x06 or I == 0x0e or I == 0x16 or I == 0x1e or I == 0x26 or I == 0x2e or I == 0x36 or I == 0x3e:
            self.MVI(Mem)
        elif I == 0xc6:
            self.ADI(Mem)
        elif I == 0xe6:
            self.ANI(Mem)
        elif I == 0xee:
            self.XRI(Mem)
        elif I == 0xf6:
            self.ORI(Mem)
        elif I == 0x2f:
            self.CMA()
        elif I == 0x27:
            self.DAA()
        elif I in range(0x80,0x86) or I == 0x87:
            self.ADD(Mem)
        elif I in range(0xa,0xa6) or I == 0xa7:
            self.ANA(Mem)
        elif I in range(0xa8,0xae) or I == 0xaf:
            self.XRA(Mem)
        elif I in range(0xb0,0xb6) or I == 0xb7:
            self.ORA(Mem)
        elif I in range(0x40, 0x76) or I in range(0x77, 0x80):
           self.MOV(Mem)
        elif I == 0x76:
            self.HALT()
        else:
            print("Opcode desconocido")
        self.plusOnePC(Mem)
        return
    #DDDSSS
    def getSSS(self, value):
        return (value & 0x07)

    def getDDD(self, value):
        return (value & 0x38) >> 3
        
    def HALT(self):
        self.halt = True

    def MOV(self,Mem):
        r = self.getDDD(self.I)
        s = self.getSSS(self.I)

        if s is not 6:
            self.setRegister(self.Indexes[r],self.getRegister(self.Indexes[s]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            position = (H<<4) | L
            if r == 6:
                Mem.setMemory(position,self.getRegister(self.Indexes[s]))
            elif s == 6:
                self.setRegister(self.Indexes[r],Mem.getMemory(position))
            

    def MVI(self, Mem):
        print("MVI")
        r = self.getDDD(self.I)
        self.plusOnePC(Mem)
        if(r is not 6):
            # b c d e h l m a
            self.setRegister(self.Indexes[r], Mem.getMemory(self.PC.getValue()))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            Mem.setMemory((H << 4) | L, Mem.getMemory(self.PC.getValue()))
    
    def ADD(self,Mem):
        print("ADD")
        r = self.getSSS(self.I)
        self.ALU.setOP1(self.getRegister("A"))

        if(r is not 6):
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP2(Mem.getMemory((H << 4) | L))  
        
        self.setRegister("A",self.ALU.ADD())


    def ADI(self, Mem):
        print("ADI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.PC.getValue()))
        self.setRegister("A", self.ALU.ADD())

    def ANI(self, Mem):
        print("ANI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.PC.getValue()))
        self.setRegister("A", self.ALU.AND())
    
    def ANA(self,Mem):
        print("ANA")
        r = self.getSSS(self.I)
        self.ALU.setOP1(self.getRegister("A"))
        if r is not 6:
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP2(Mem.getMemory((H << 4) | L)) 
        self.setRegister("A",self.ALU.AND())

        

    def ORI(self, Mem):
        print("ORI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.PC.getValue()))
        self.setRegister("A", self.ALU.OR())

    def ORA(self,Mem):
        print("XRA")
        r = self.getSSS(self.I)
        self.ALU.setOP1(self.getRegister("A"))
        if r is not 6:
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP2(Mem.getMemory((H << 4) | L)) 
        self.setRegister("A",self.ALU.OR())

    def CMA(self):
        print("CMA")
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A", self.ALU.NOT())

    def XRI(self, Mem):
        print("XRI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.PC.getValue()))
        self.setRegister("A", self.ALU.XOR())
    
    def XRA(self,Mem):
        print("XRA")
        r = self.getSSS(self.I)
        self.ALU.setOP1(self.getRegister("A"))
        if r is not 6:
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP2(Mem.getMemory((H << 4) | L)) 
        self.setRegister("A",self.ALU.XOR())

    def DAA(self):
        print("DAA")
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A",self.ALU.BCD())

    def RLC(self):
        print("RLC")
        A = self.getRegister("A")
        self.ALU.setOP1(A)
        self.setRegister("A",self.ALU.RLC())
    
    def RRC(self):
        print("RRC")
        A = self.getRegister("A")
        self.ALU.setOP1(A)
        self.setRegister("A",self.ALU.RRC())


'''
OP 0X07
rlc
bits a la izquierda 
m 0 v 7 a 128
si el bit mas significativo vale 1, activar carry
____
OP 0x0f
rrc
bits a la derecha, bit mas significativo va al principio y activar carry dependiendo si esta activado
___
op 0x17
RAL
___
op 0x1f
RAR
'''


# 0xf6
'''
    SBI SUB

    ======== Done
    *MOV
    *DAA
    *ORA
    *XRA
    *ANA
    *ADD
    *HLT
    *NOP
    *CMA
    *MVI
    *ANI
    *XRI
    *ORI
    *ADI
'''


if __name__ == "__main__":
    mem = Memory(2**2)
    # testing write
    '''
    mem.setMemory(0, 198)
    mem.setMemory(1, 6)
    mem.setMemory(2, 0)
    mem.Write("file.bin")
    mem.Load("file.bin")
    '''
    cpu = CPU()
    cpu.execute(mem)
    cpu.execute(mem)
    cpu.execute(mem)
    cpu.execute(mem)
