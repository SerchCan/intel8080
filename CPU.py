from Registros import Registros
from Registro import Registro
from ALU import ALU
from Memoria import Memory


class CPU:
    def __init__(self):
        self.ALU = ALU()
        self.PC = Registro(0x0000)
        self.SP = Registro(0xf000)
        self.REGISTERS = Registros()
        self.halt = False
        self.INTE = False #if True not allow interruptions
        self.interruptionNumber = 0
        self.I = 0
        self.Indexes = ["B", "C", "D", "E", "H", "L", "M", "A"]

    def setInterruptionNumber(self,number):
        self.interruptionNumber = number
       
    def getStatus(self):
        return self.halt

    def setStatus(self, halt):
        self.halt = halt

    def getALU(self):
        return self.ALU

    def getPC(self):
        return self.PC.getValue()

    def getSP(self):
        return self.SP.getValue()

    def getRegister(self,index):
        return self.REGISTERS.getRegister(index)

    def getRegisters(self):
        return self.REGISTERS
        
    def setRegister(self, index, value):
        self.REGISTERS.setRegister(index, value)

    def setPC(self, value,Mem):
        self.PC.setValue(value % Mem.getSize()) 

    def setSP(self, value,Mem):
        self.SP.setValue(value % Mem.getSize())

    def plusOnePC(self,Mem):
        self.PC.setValue( (self.getPC()+1)%Mem.getSize())

    def execute(self, Mem, Ports):
        pc = self.getPC()
        self.I = Mem.getMemory(pc)

        I = self.I
        if I in [0x00,0x10,0x20,0x30,0x08,0x18,0x28,0x38]:
            self.NOP(Mem)
        elif I == 0x07:
            self.RLC(Mem)
        elif I == 0x17:
            self.RAL(Mem)
        elif I == 0x0f:
            self.RRC(Mem)
        elif I == 0x1f:
            self.RAR(Mem)
        elif I in [0x06, 0x0e, 0x16, 0x1e, 0x26, 0x2e, 0x36, 0x3e]:
            self.MVI(Mem)
        elif I == 0xce:
            self.ACI(Mem)
        elif I == 0xc6:
            self.ADI(Mem)
        elif I == 0xd6:
            self.SUI(Mem)
        elif I == 0xde:
            self.SBI(Mem)
        elif I == 0xe6:
            self.ANI(Mem)
        elif I == 0xee:
            self.XRI(Mem)
        elif I == 0xf6:
            self.ORI(Mem)
        elif I == 0x2f:
            self.CMA(Mem)
        elif I == 0x27:
            self.DAA(Mem)
        elif I == 0x3a:
            self.LDA(Mem)
        elif I == 0xe3:
            self.XTHL(Mem)
        elif I == 0xc3:
            self.JMP(Mem)
        elif I == 0xda:
            self.JC(Mem)
        elif I == 0xd2:
            self.JNC(Mem)
        elif I == 0xfa:
            self.JM(Mem)
        elif I == 0xf2:
            self.JP(Mem)
        elif I == 0xe2:
            self.JPO(Mem)
        elif I == 0xea:
            self.JPE(Mem)
        elif I == 0xca:
            self.JZ(Mem)
        elif I == 0xc2:
            self.JNZ(Mem)
        elif I == 0xe9:
            self.PCHL(Mem)
        elif I == 0x2a:
            self.LHLD(Mem)
        elif I == 0x22:
            self.SHLD(Mem)
        elif I == 0xeb:
            self.XCHG(Mem)
        elif I == 0xcd:
            self.CALL(Mem)
        elif I == 0xdc:
            self.CC(Mem)
        elif I == 0xd4:
            self.CNC(Mem)
        elif I == 0xf4:
            self.CP(Mem)
        elif I == 0xfc:
            self.CM(Mem)
        elif I == 0xec:
            self.CPE(Mem)
        elif I == 0xe4:
            self.CPO(Mem)
        elif I == 0xc4:
            self.CNZ(Mem)
        elif I == 0xcc:
            self.CZ(Mem)
        elif I == 0xc9:
            self.RET(Mem)
        elif I == 0xd8:
            self.RC(Mem)
        elif I == 0xd0:
            self.RNC(Mem)
        elif I == 0xc8:
            self.RZ(Mem)
        elif I == 0xc0:
            self.RNZ(Mem)
        elif I == 0xf0:
            self.RP(Mem)
        elif I == 0xf8:
            self.RM(Mem)
        elif I == 0xe8:
            self.RPE(Mem)
        elif I == 0xe0:
            self.RPO(Mem)
        elif I == 0xf3:
            self.DI(Mem)
        elif I == 0xfb:
            self.EI(Mem)
        elif I == 0xf9:
            self.SPHL(Mem)
        elif I == 0xdb:
            self.IN(Mem,Ports)
        elif I == 0x3f:
            self.CMC(Mem)
        elif I == 0xfe:
            self.CPI(Mem)
        elif I == 0x37:
            self.STC(Mem)
        elif I == 0x32:
            self.STA(Mem)
        elif I == 0xd3:
            self.OUT(Mem,Ports)
        elif I in [0x0a,0x1a]:
            self.LDAX(Mem)
        elif I in [0x01,0x11,0x21,0x31]:
            self.LXI(Mem)
        elif I in [0x02,0x12]:
            self.STAX(Mem)
        elif I in [0x04,0x0c,0x14,0x1c,0x24,0x2c,0x34,0x3c]:
            self.INR(Mem)
        elif I in [0x05,0x0d,0x15,0x1d,0x25,0x2d,0x35,0x3d]:
            self.DCR(Mem)
        elif I in [0xc7,0xcf,0xd7,0xdf,0xe7,0xef,0xf7,0xff]:
            self.RST(Mem)
        elif I in [0xc5,0xd5,0xe5,0xf5]:
            self.PUSH(Mem)
        elif I in [0xc1,0xd1,0xe1,0xf1]:
            self.POP(Mem)
        elif I in [0x03, 0x13, 0x23, 0x33]:
            self.INX(Mem)
        elif I in [0x0b, 0x1b, 0x2b, 0x3b]:
            self.DCX(Mem)
        elif I in [0x09,0x19,0x29,0x39]:
            self.DAD(Mem)
        elif I in range(0xb8,0xc0):
            self.CMP(Mem)
        elif I in range(0x98,0xa0):
            self.SBB(Mem)
        elif I in range(0x88, 0x90):
            self.ADC(Mem)
        elif I in range(0x80,0x88):
            self.ADD(Mem)
        elif I in range(0x90,0x98):
            self.SUB(Mem)
        elif I in range(0xa0,0xa8):
            self.ANA(Mem)
        elif I in range(0xa8,0xb0):
            self.XRA(Mem)
        elif I in range(0xb0,0xb8):
            self.ORA(Mem)
        elif I in range(0x40, 0x76) or I in range(0x77, 0x80):
           self.MOV(Mem)
        elif I == 0x76:
            self.HALT()
        else:
            print("Opcode desconocido")
            #self.NOP(Mem)

        if self.INTE:
            self.hardware_restart(Mem,self.interruptionNumber)
            self.EI(Mem)
        return

    def getInterruptionNumber(self):
        return (self.I & 0x0038) >> 3
        
    def hardware_restart(self,Mem,numberOfInterruption):
        bitshift = self.I & 0xc7
        self.I = Mem.getMemory(bitshift) | (numberOfInterruption << 3)
        self.RST(Mem)
    
    #DDDSSS
    def getSSS(self, value):
        return (value & 0x07)

    def getDDD(self, value):
        return (value & 0x38) >> 3
    # --XX----
    def getXXPushPop(self,value):
        return(value & 0x30) >> 4

    def HALT(self):
        print("HALT")
        self.halt = True

    def NOP(self,Mem):
        print("NO OP")
        self.plusOnePC(Mem)
    def MOV(self,Mem):
        print("MOV")
        r = self.getDDD(self.I)
        s = self.getSSS(self.I)
        if r!=6 and s != 6:
            self.setRegister(self.Indexes[r],self.getRegister(self.Indexes[s]))
        elif r!=6 and s == 6:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            position = self.ALU.doMemoryPair()

            yy = Mem.getMemory(position)
            self.setRegister(self.Indexes[r],yy)

        elif r==6 and s!=6:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            position = self.ALU.doMemoryPair()

            yy = self.getRegister(self.Indexes[s])
            Mem.setMemory(position,yy)
        self.plusOnePC(Mem)    

    def MVI(self, Mem):
        print("MVI")
        r = self.getDDD(self.I)
        self.plusOnePC(Mem)
        xx = Mem.getMemory(self.getPC())
        if(r is not 6):
            # b c d e h l m a
            self.setRegister(self.Indexes[r], xx)
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            Mem.setMemory(self.ALU.doMemoryPair(), xx)
        self.plusOnePC(Mem)    
    
    def ADD(self,Mem):
        print("ADD")
        r = self.getSSS(self.I)

        if(r is not 6):
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            self.ALU.setOP2(Mem.getMemory(self.ALU.doMemoryPair))  
        
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A",self.ALU.ADD())
        self.plusOnePC(Mem)    

    def ADI(self, Mem):
        print("ADI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.getPC()))
        self.setRegister("A", self.ALU.ADD())
        self.plusOnePC(Mem)    

    def ANI(self, Mem):
        print("ANI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.getPC()))
        self.setRegister("A", self.ALU.AND())
        self.plusOnePC(Mem)    
    
    def ANA(self,Mem):
        print("ANA")
        r = self.getSSS(self.I)
        if r is not 6:
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            
            self.ALU.setOP2(Mem.getMemory(self.ALU.doMemoryPair())) 

        self.ALU.setOP1(self.getRegister("A"))
        
        self.setRegister("A",self.ALU.AND())
        self.plusOnePC(Mem)    

    def SUB(self,Mem):
        print("SUB")
        r = self.getSSS(self.I)

        if(r is not 6):
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            
            self.ALU.setOP2(Mem.getMemory(self.ALU.doMemoryPair()))
            
        self.ALU.setOP1(self.getRegister("A"))
        
        self.setRegister("A",self.ALU.SUB())
        self.plusOnePC(Mem)   
    
    def CMP(self,Mem):
        print("CMP")
        r = self.getSSS(self.I)

        if(r is not 6):
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            
            self.ALU.setOP2(Mem.getMemory(self.ALU.doMemoryPair()))
        #probably set flags on 0 c Ac
        self.ALU.setOP1(self.getRegister("A"))
        self.ALU.SUB()
        self.plusOnePC(Mem)   
    
    def CPI(self,Mem):
        print("CPI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.getPC()))
        self.ALU.SUB()
        self.plusOnePC(Mem)

    def SBI(self,Mem):
        print("SBI")
        self.plusOnePC(Mem)
        yy = Mem.getMemory(self.getPC())
        self.ALU.setOP1(yy)
        self.ALU.setOP2(self.getRegister("A"))
        
        carry = 0
        if  self.ALU.getFlags().getFlag("C"):
            carry=1

        self.setRegister("A",self.ALU.SUB(carry=carry))
        self.plusOnePC(Mem)

    def ORI(self, Mem):
        print("ORI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.getPC()))
        self.setRegister("A", self.ALU.OR())
        self.plusOnePC(Mem)    

    def ORA(self,Mem):
        print("ORA")
        r = self.getSSS(self.I)
        if r is not 6:
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            
            self.ALU.setOP2(Mem.getMemory(self.ALU.doMemoryPair()))
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A",self.ALU.OR())
        self.plusOnePC(Mem)    

    def CMA(self,Mem):
        print("CMA")
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A", self.ALU.NOT())
        self.plusOnePC(Mem)    

    def XRI(self, Mem):
        print("XRI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.getPC()))
        self.setRegister("A", self.ALU.XOR())
        self.plusOnePC(Mem)    
    
    def XRA(self,Mem):
        print("XRA")
        r = self.getSSS(self.I)
        if r is not 6:
            self.ALU.setOP2(self.getRegister(self.Indexes[r]))
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            
            self.ALU.setOP2(Mem.getMemory(self.ALU.doMemoryPair()))
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A",self.ALU.XOR())
        self.plusOnePC(Mem)    

    def DAA(self,Mem):
        print("DAA")
        self.ALU.setOP1(self.getRegister("A"))
        self.setRegister("A",self.ALU.BCD())
        self.plusOnePC(Mem)    

    def RLC(self,Mem):
        print("RLC")
        A = self.getRegister("A")
        self.ALU.setOP1(A)
        self.setRegister("A",self.ALU.RLC())
        self.plusOnePC(Mem)    

    def RAL(self,Mem):
        print("RAL")
        A = self.getRegister("A")
        C = (A & 0x80) >> 7
        self.ALU.getFlags().setFlag("C",C)
        F = self.ALU.getFlags().getFlag("C")
        A = (A << 1) & 0xff
        self.setRegister("A",A|F)
        self.plusOnePC(Mem)    

    def RRC(self,Mem):
        print("RRC")
        A = self.getRegister("A")
        self.ALU.setOP1(A)
        self.setRegister("A",self.ALU.RRC())
        self.plusOnePC(Mem)    

    def RAR(self,Mem):
        print("RAR")
        A = self.getRegister("A")
        C = (A & 0x01)
        self.ALU.getFlags().setFlag("C",C)
        F = self.ALU.getFlags().getFlag("C")
        A = (A >> 1) & 0xff
        self.setRegister("A",A|(F<<7))
        self.plusOnePC(Mem)    

    def DecodeAluPair(self,value):
        high = (value & 0xFF00) >> 8
        low = (value & 0x00FF)
        return high,low

    def DecodeRegisterPair(self, I):
        return (I & 0x30) >> 4
    
    def INX(self,Mem):
        print("INCX")
        r = self.DecodeRegisterPair(self.I)
        #bc, de, hl
        if(r==0):
            self.ALU.setOP1(self.getRegister("B"))
            self.ALU.setOP2(self.getRegister("C"))
            B,C = self.DecodeAluPair(self.ALU.INX())
            self.setRegister("B",B)
            self.setRegister("C",C)
        elif r==1:
            self.ALU.setOP1(self.getRegister("D"))
            self.ALU.setOP2(self.getRegister("E"))
            D,E = self.DecodeAluPair(self.ALU.INX())
            self.setRegister("D",D)
            self.setRegister("E",E)
        elif r==2:
            self.ALU.setOP1(self.getRegister("H"))
            self.ALU.setOP2(self.getRegister("L"))
            H,L = self.DecodeAluPair(self.ALU.INX())
            self.setRegister("H",H)
            self.setRegister("L",L)
        else:
            self.ALU.setOP1(self.SP.getValue())
            catcher = self.ALU.INX(False)
            self.SP.setValue(catcher)
        self.plusOnePC(Mem)
    
    def DCX(self,Mem):
        print("DCX")
        r = self.DecodeRegisterPair(self.I)
        #bc, de, hl
        if(r==0):
            self.ALU.setOP1(self.getRegister("B"))
            self.ALU.setOP2(self.getRegister("C"))
            B,C = self.DecodeAluPair(self.ALU.DCX())
            self.setRegister("B",B)
            self.setRegister("C",C)
        elif r==1:
            self.ALU.setOP1(self.getRegister("D"))
            self.ALU.setOP2(self.getRegister("E"))
            D,E = self.DecodeAluPair(self.ALU.DCX())
            self.setRegister("D",D)
            self.setRegister("E",E)
        elif r==2:
            self.ALU.setOP1(self.getRegister("H"))
            self.ALU.setOP2(self.getRegister("L"))
            H,L = self.DecodeAluPair(self.ALU.DCX())
            self.setRegister("H",H)
            self.setRegister("L",L)
        else:
            self.ALU.setOP1(self.SP.getValue())
            catcher = self.ALU.DCX(False)
            self.SP.setValue(catcher)
        self.plusOnePC(Mem)   

    def regPairMask(self,I):
        return (I & 0x10)>>4

    def LDAX(self,Mem) :
        print("LDAX")
        I = self.I
        r = self.regPairMask(I)
        memPos = 0
        if r == 0:
            self.ALU.setOP1(self.getRegister("B"))
            self.ALU.setOP2(self.getRegister("C"))
        else:
            self.ALU.setOP1(self.getRegister("D"))
            self.ALU.setOP2(self.getRegister("E"))
        
        memPos =  self.ALU.doMemoryPair()

        self.setRegister("A",Mem.getMemory(memPos))
        self.plusOnePC(Mem)
    
    def STAX(self,Mem):
        print("STAX")
        I = self.I
        r = self.regPairMask(I)
        memPos = 0
        if r == 0:
            self.ALU.setOP1(self.getRegister("B"))
            self.ALU.setOP2(self.getRegister("C"))
            memPos =  self.ALU.doMemoryPair()
        else:
            self.ALU.setOP1(self.getRegister("D"))
            self.ALU.setOP2(self.getRegister("E"))
            memPos =  self.ALU.doMemoryPair()
        
        Mem.setMemory(memPos,self.getRegister("A"))
        self.plusOnePC(Mem)
    def JMP(self,Mem):
        print("JMP")
        qq = Mem.getMemory(self.getPC()+1)
        pp = Mem.getMemory(self.getPC()+2)
        
        self.ALU.setOP1(pp)
        self.ALU.setOP2(qq)
            
        newPC = self.ALU.doMemoryPair()
        
        self.ALU.getFlags().setFlag("C",True)
        self.setPC(newPC,Mem)
    
    def JC(self,Mem):
        print("JC")
        if(self.ALU.getFlags().getFlag("C")):
            self.JMP(Mem)
        else:
            self.setPC((self.getPC()+3 ),Mem)
    
    def JNC(self,Mem):
        print("JNC")
        if(self.ALU.getFlags().getFlag("C")):
            self.setPC((self.getPC()+3 ),Mem)
        else:
            self.JMP(Mem)

    def JP(self,Mem):
        print("JP")
        if(self.ALU.getFlags().getFlag("S")):
            self.setPC((self.getPC()+3 ),Mem)
        else:
            self.JMP(Mem)
    
    def JM(self,Mem):
        print("JM")
        if(self.ALU.getFlags().getFlag("S")):
            self.JMP(Mem)
        else:
            self.setPC((self.getPC()+3 ),Mem)
    
    def JPO(self,Mem):
        print("JPO")
        if(self.ALU.getFlags().getFlag("P")):
            self.setPC((self.getPC()+3 ),Mem)
        else:
            self.JMP(Mem)
    
    def JPE(self,Mem):
        print("JPE")
        if(self.ALU.getFlags().getFlag("P")):
            self.JMP(Mem)
        else:
            self.setPC((self.getPC()+3 ),Mem)
    
    def JZ(self,Mem):
        print("JZ")
        if(self.ALU.getFlags().getFlag("Z")):
            self.JMP(Mem)
        else:
            self.setPC((self.getPC()+3),Mem)
    
    def JNZ(self,Mem):
        print("JNZ")
        if(self.ALU.getFlags().getFlag("Z")):
            self.setPC((self.getPC()+3),Mem)
        else:
            self.JMP(Mem)
        
    def PCHL(self,Mem):
        print("PCHL")
        H = self.getRegister("H")
        L = self.getRegister("L")
        self.ALU.setOP1(H)
        self.ALU.setOP2(L)
        position = self.ALU.doMemoryPair()
        self.setPC(position,Mem)

    def LHLD(self,Mem):
        print("LHLD")
        self.plusOnePC(Mem)
        qq = Mem.getMemory(self.getPC())
        self.plusOnePC(Mem)
        pp = Mem.getMemory(self.getPC())

        self.ALU.setOP1(pp)
        self.ALU.setOP2(qq)
        ppqq = self.ALU.doMemoryPair()

        xx = Mem.getMemory(ppqq)
        yy = Mem.getMemory(ppqq+1)
        self.setRegister("H",yy)
        self.setRegister("L",xx)
        self.plusOnePC(Mem)
    
    def SHLD(self,Mem):
        print("SHLD")
        self.plusOnePC(Mem)
        qq = Mem.getMemory(self.getPC())
        self.plusOnePC(Mem)
        pp = Mem.getMemory(self.getPC())

        self.ALU.setOP1(pp)
        self.ALU.setOP2(qq)
        ppqq = self.ALU.doMemoryPair()

        H = self.getRegister("H")
        L = self.getRegister("L")
        Mem.setMemory(ppqq,L)
        Mem.setMemory(ppqq+1,H)
        self.plusOnePC(Mem)

    def XCHG(self,Mem):
        print("XCHG")
        D = self.getRegister("D")
        E = self.getRegister("E")

        self.setRegister("D",self.getRegister("H"))
        self.setRegister("E",self.getRegister("L"))

        self.setRegister("H",D)
        self.setRegister("L",E)
        self.plusOnePC(Mem)

    def SPHL(self,Mem):
        print("SPHL")
        H = self.getRegister("H")
        L = self.getRegister("L")
        self.ALU.setOP1(H)
        self.ALU.setOP2(L)
        position = self.ALU.doMemoryPair()
        self.setSP(position,Mem)
        self.plusOnePC(Mem)

    def PUSH(self,Mem):
        print("PUSH")
        I = self.I
        r = self.getXXPushPop(I)

        self.setSP(self.getSP()-2,Mem)
        qq = 0
        pp = 0
        
        if r == 0:
            qq = self.getRegister("C")
            pp = self.getRegister("B")
        elif r == 1:
            qq = self.getRegister("E")
            pp = self.getRegister("D")
        elif r == 2:
            qq = self.getRegister("L")
            pp = self.getRegister("H")
        elif r == 3:
            PSW = self.ALU.getFlags().getPSWRegister()
            qq = PSW
            pp = self.getRegister("A")
        
        Mem.setMemory(self.getSP(),qq)
        Mem.setMemory(self.getSP()+1,pp)
        self.plusOnePC(Mem)
    
    def POP(self,Mem):
        print("POP")
        I = self.I
        r = self.getXXPushPop(I)
        sp = self.getSP()

        YY = Mem.getMemory(sp)
        XX = Mem.getMemory(sp+1)

        if r == 0:
            self.setRegister("C",YY)
            self.setRegister("B",XX)
        elif r == 1:
            self.setRegister("E",YY)
            self.setRegister("D",XX)
        elif r == 2:
            self.setRegister("L",YY)
            self.setRegister("H",XX)
        elif r == 3:
            print("listYY",YY)
            binValue=bin(YY)[2:]
            var = ""
            if len(binValue)<8:
                for i in range(8-len(binValue)):
                    var+="0"
            var += binValue
            self.ALU.getFlags().setPSWRegister(list(var))
            self.setRegister("A",XX)
        
        self.setSP(sp+2,Mem)
        self.plusOnePC(Mem)

    def CALL(self,Mem):
        print("CALL")
        
        self.setSP(self.getSP()-2,Mem)

        self.plusOnePC(Mem)
        qq=Mem.getMemory(self.getPC()) #PC+1)
        self.plusOnePC(Mem)
        pp=Mem.getMemory(self.getPC()) #PC+2)
        self.plusOnePC(Mem)

        mm,mPlus3 = self.DecodeAluPair(self.getPC()) # mmmm+3
        Mem.setMemory(self.getSP(),mPlus3)
        Mem.setMemory(self.getSP()+1,mm)
        
        
        
        self.ALU.setOP1(pp)
        self.ALU.setOP2(qq)
        newPC=self.ALU.doMemoryPair()
        
        self.setPC(newPC,Mem)
       
        return

    def CC(self,Mem):
        print("CC")
        if self.ALU.getFlags().getFlag("C"):
            self.CALL(Mem)
        else:
            self.setPC(self.getPC()+3,Mem)
    
    def CNC(self,Mem):
        print("CNC")
        if self.ALU.getFlags().getFlag("C"):
            self.setPC(self.getPC()+3,Mem)
        else:
            self.CALL(Mem)


    def CZ (self,Mem):
        print("CZ")
        if self.ALU.getFlags().getFlag("Z") :
            self.CALL(Mem)
        else:
            self.setPC(self.getPC()+3,Mem)

    def CNZ(self,Mem):
        print("CNZ")
        if self.ALU.getFlags().getFlag("Z") :
            self.CALL(Mem)
        else:
            self.setPC(self.getPC()+3,Mem)


    def CP (self,Mem):
        print("CP")
        if self.ALU.getFlags().getFlag("S") :
            self.setPC(self.getPC()+3,Mem)
        else:
            self.CALL(Mem)

    def CM(self,Mem):
        print("CM")
        if self.ALU.getFlags().getFlag("S") :
            self.CALL(Mem)
        else:
            self.setPC(self.getPC()+3,Mem)


    def CPE (self,Mem):
        print("CPE")
        if self.ALU.getFlags().getFlag("P") :
            self.CALL(Mem)
        else:
            self.setPC(self.getPC()+3,Mem)

    def CPO(self,Mem):
        print("CPO")
        if self.ALU.getFlags().getFlag("P") :
            self.setPC(self.getPC()+3,Mem)
        else:
            self.CALL(Mem)

    def RET(self,Mem):
        print("RET")
        sp = self.getSP()
        qq= Mem.getMemory(sp)
        pp= Mem.getMemory(sp+1)
        
        self.ALU.setOP1(pp)
        self.ALU.setOP2(qq)
        
        self.setPC(self.ALU.doMemoryPair(),Mem)
        self.setSP(sp+2,Mem)
      
    def RC(self,Mem):
        print("RC")
        if self.ALU.getFlags().getFlag("C"):
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)
    
    def RNC(self,Mem):
        print("RNC")
        if self.ALU.getFlags().getFlag("C"):
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)


    def RZ (self,Mem):
        print("RZ")
        if self.ALU.getFlags().getFlag("Z") :
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)

    def RNZ(self,Mem):
        print("RNZ")
        if self.ALU.getFlags().getFlag("Z") :
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)


    def RP (self,Mem):
        print("RP")
        if self.ALU.getFlags().getFlag("S") :
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)

    def RM(self,Mem):
        print("RM")
        if self.ALU.getFlags().getFlag("S") :
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)


    def RPE (self,Mem):
        print("RPE")
        if self.ALU.getFlags().getFlag("P") :
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)

    def RPO(self,Mem):
        print("RPO")
        if self.ALU.getFlags().getFlag("P") :
            self.RET(Mem)
        else:
            self.plusOnePC(Mem)

    def DI(self,Mem):
        print("DI")
        self.INTE = True
        self.plusOnePC(Mem)

    def EI(self,Mem):
        print("EI")
        self.INTE = False
        self.plusOnePC(Mem)

    def IN(self,Mem,Ports):
        print("IN")
        self.plusOnePC(Mem)
        
        yy = Mem.getMemory(self.getPC())
        xx = Ports.getPort(yy)

        self.setRegister("A",xx)
        self.plusOnePC(Mem)

    def OUT(self,Mem,Ports):
        print("OUT")
        self.plusOnePC(Mem)
        
        yy = Mem.getMemory(self.getPC())
        xx = self.getRegister("A")
        
        Ports.setPort(yy,xx)
        self.plusOnePC(Mem)

    def RST(self,Mem):
        print("RST")
        self.setSP(self.getSP()-2,Mem)
        mmmmp2=self.getPC()+2
        mm, mp2 = self.DecodeAluPair(mmmmp2)

        Mem.setMemory(self.getSP(),mp2)
        Mem.setMemory(self.getSP()+1,mm)
        
        self.setPC(self.getInterruptionNumber(),Mem)

    def CMC(self,Mem):
        print("CMC")
        if self.getALU().getFlags().getFlag("C"):
            self.getALU().getFlags().setFlag("C",False)
        else:
            self.getALU().getFlags().setFlag("C",True)
        self.plusOnePC(Mem)
    
    def DAD(self,Mem):
        print("DAD")
        I = self.I
        xx = self.getXXPushPop(I)
        if xx == 0:
            y1 = self.getRegister("B")
            y2 = self.getRegister("C")
        elif xx == 1:
            y1 = self.getRegister("D")
            y2 = self.getRegister("E")
        elif xx == 3:
            y1 = self.getRegister("H")
            y2 = self.getRegister("L")
        else:
            y1,y2 = self.DecodeAluPair(self.getSP())
        
        self.ALU.setOP1(self.getRegister("H"))
        self.ALU.setOP2(y1)
        self.setRegister("H",self.ALU.ADD())

        self.ALU.setOP1(self.getRegister("L"))
        self.ALU.setOP2(y2)
        self.setRegister("L",self.ALU.ADD())

        self.plusOnePC(Mem)
    
    def DCR(self,Mem):
        print("DCR")
        I = self.I
        r = self.getDDD(I)
        B = 0 if self.ALU.getFlags().getFlag("C") else 1
        if r is not 6:
            self.ALU.setOP1(self.getRegister(self.Indexes[r]))
            self.ALU.setOP2(0x01)
            self.setRegister(self.Indexes[r],self.ALU.SUB(B))
        else:
            self.ALU.setOP1(self.getRegister("H"))
            self.ALU.setOP2(self.getRegister("L"))
            ppqq = self.ALU.doMemoryPair()

            self.ALU.setOP1(Mem.getMemory(ppqq))
            self.ALU.setOP2(0x01)
            Mem.setMemory(ppqq,self.ALU.SUB(B))
        self.plusOnePC(Mem)
        
    def INR(self,Mem):
        print("INR")
        I = self.I
        r = self.getDDD(I)
        if r is not 6:
            self.ALU.setOP1(self.getRegister(self.Indexes[r]))
            self.ALU.setOP2(0x01)
            self.setRegister(self.Indexes[r],self.ALU.ADD())
        else:
            self.ALU.setOP1(self.getRegister("H"))
            self.ALU.setOP2(self.getRegister("L"))
            ppqq = self.ALU.doMemoryPair()

            self.ALU.setOP1(Mem.getMemory(ppqq))
            self.ALU.setOP2(0x01)
            Mem.setMemory(ppqq,self.ALU.ADD())
        self.plusOnePC(Mem)

    def LDA(self,Mem):
        print("LDA")
        self.plusOnePC(Mem)
        qq = Mem.getMemory(self.getPC())
        self.plusOnePC(Mem)
        pp = Mem.getMemory(self.getPC())

        self.ALU.setOP1(pp)
        self.ALU.setOP2(qq)

        ppqq = self.ALU.doMemoryPair()

        self.setRegister("A",Mem.getMemory(ppqq))
        self.plusOnePC(Mem)

    def LXI(self,Mem):
        print("LXI")
        I = self.I
        xx = self.getXXPushPop(I)

        self.plusOnePC(Mem)
        qq = Mem.getMemory(self.getPC())
        self.plusOnePC(Mem)
        pp = Mem.getMemory(self.getPC())
        if xx == 0:
            self.setRegister("B",pp)
            self.setRegister("C",qq)
        elif xx == 1:
            self.setRegister("D",pp)
            self.setRegister("E",qq)
        elif xx == 2:
            self.setRegister("H",pp)
            self.setRegister("L",qq)
        else: 
            self.ALU.setOP1(pp)
            self.ALU.setOP2(qq)
            self.setSP(self.ALU.doMemoryPair(),Mem)
        self.plusOnePC(Mem)
    
    def STA(self,Mem):
        print("STA")
        self.plusOnePC(Mem)
        qq = Mem.getMemory(self.getPC())
        self.plusOnePC(Mem)
        pp = Mem.getMemory(self.getPC())

        self.ALU.setOP1(pp)
        self.ALU.setOP1(qq)
        ppqq = self.ALU.doMemoryPair()

        Mem.setMemory(ppqq,self.getRegister("A"))

        self.plusOnePC(Mem)

    def STC(self,Mem):
        print("STC")
        self.ALU.getFlags().setFlag("C",True)
        self.plusOnePC(Mem)
    
    def XTHL(self,Mem):
        print("XTHL")
        ssss = self.getSP()

        rr = Mem.getMemory(ssss)
        t1 = self.getRegister("H")

        ss = Mem.getMemory(ssss+1)
        t2 = self.getRegister("L")

        pp,qq = t1,t2

        self.setRegister("H",rr)
        self.setRegister("L",ss)

        Mem.setMemory(ssss,pp)
        Mem.setMemory(ssss+1,qq)

        self.plusOnePC(Mem)

    def ACI(self, Mem):
        print("ACI")
        C = 0
        if self.ALU.getFlags().getFlag("C"):
            C = 1
        xx = self.getRegister("A")
        self.plusOnePC(Mem)
        yy = Mem.getMemory(self.getPC())

        self.ALU.setOP1(C)
        self.ALU.setOP2(xx)

        self.ALU.setOP1(self.ALU.ADD())
        self.ALU.setOP2(yy)

        self.setRegister("A",self.ALU.ADD())
        self.plusOnePC(Mem)

    def ADC(self, Mem):
        print("ADC")
        I = self.I
        sss = self.getSSS(I)
        C = 0
        if self.ALU.getFlags().getFlag("C"):
            C = 1

        xx = self.getRegister("A")
        if sss is not 6:
            yy = self.getRegister(self.Indexes[sss])
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            ppqq = self.ALU.doMemoryPair()
            yy = Mem.getMemory(ppqq)

        self.ALU.setOP1(C)
        self.ALU.setOP2(xx)
        self.ALU.setOP1(self.ALU.ADD())
        self.ALU.setOP2(yy)
        self.setRegister("A",self.ALU.ADD())

        self.plusOnePC(Mem)

    def SBB(self,Mem):
        print("SBB")
        I = self.I

        sss = self.getSSS(I)
        B = 0
        if self.ALU.getFlags().getFlag("C"):
            B = 1

        xx = self.getRegister("A")
        if sss is not 6:
            yy = self.getRegister(self.Indexes[sss])
        else:
            H = self.getRegister("H")
            L = self.getRegister("L")
            self.ALU.setOP1(H)
            self.ALU.setOP2(L)
            ppqq = self.ALU.doMemoryPair()
            yy = Mem.getMemory(ppqq)

        self.ALU.setOP1(xx)
        self.ALU.setOP2(yy)
        self.setRegister("A",self.ALU.SUB(B))

        self.plusOnePC(Mem)

    def SUI(self, Mem):
        print("SUI")
        self.ALU.setOP1(self.getRegister("A"))
        self.plusOnePC(Mem)
        self.ALU.setOP2(Mem.getMemory(self.getPC()))
        self.setRegister("A", self.ALU.SUB())
        self.plusOnePC(Mem)  
    
'''
___

SUB family
sui

'''

# 0xf6
'''
    ======== Done
    *INX
    *DCX
    *RLC
    *RRC
    *MOV
    *DAA
    *ORA
    *XRA
    *ANA
    *SUB
    *SBI
    *ADD
    *HLT
    *NOP
    *CMA
    *MVI
    *ANI
    *XRI
    *ORI
    *ADI
    *LDAX
    *STAX
    *JMP
    *JC JNC
    *JP JM
    *JPE JPO
    *JNZ JZ
    *PCHL
    *LHLD
    *SHLD
    *XCHG
    *SPHLs
    *PUSH
    *POP    
    *CALL
    *CC CNC
    *CZ CNZ
    *CP CNP
    *CPE CPO
    *RET
    *RC RNC
    *RZ  RNZ
    *RP RMP
    *RPE RPO
    *DI EI
    *CMC
    -- puertos son 256 --
    *IN 
    *OUT
    *RST // HW_RST
    *cmp == sub
    *cpi
    *DAD
    *DCR
    *INR
    *LDA
    *LXI
    *STA
    *STC
    *XTHL
    *ACI
    *ADC
    *sbb

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
    #cpu.execute(mem)
    #cpu.execute(mem)
    #cpu.execute(mem)
    #cpu.execute(mem)
