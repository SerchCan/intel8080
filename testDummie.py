txt = "00"

for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            n = ""
            n=str(i)+str(j)+str(k)

            print(hex(int(txt+n+"110",2)))
print("__")
txt = "00"
for i in range(0,2):
    for j in range(0,2):
        n = ""
        n=str(i)+str(j)
        print(hex(int(txt+n+"1001",2)))
def DAD(self,Mem):
        print("DAD")
        I = self.I
        xx = self.getXXPushPop(I)
        self.ALU.setOP1(self.getRegister("H"))
        self.ALU.setOP2(self.getRegister("L"))
        HL=self.ALU.doMemoryPair()
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
        
        self.ALU.setOP1(y1)
        self.ALU.setOP2(y2)
        y1y2=self.ALU.doMemoryPair()

        '''
        self.ALU.setOP1(self.getRegister("H"))
        self.ALU.setOP2(y1)
        self.setRegister("H",self.ALU.ADD())

        self.ALU.setOP1(self.getRegister("L"))
        self.ALU.setOP2(y2)
        self.setRegister("L",self.ALU.ADD())
        '''

        self.ALU.setOP1(HL)
        self.ALU.setOP2(y1y2)
        res= HL+y1y2
        if res>65536:
            self.ALU.getFlags().setFlag("C",True)    
        H,L = self.DecodeAluPair(res)
        self.setRegister("H",H)
        self.setRegister("L",L)
        self.plusOnePC(Mem)
    
'''

import numpy as np
mem = [0x01 for i in range(0x2400,0x4000)]
print(len(mem))

pixels=[]
for i in mem:
    for bit in range(7,-1,-1):
        px=(i>>bit) & 0x01
        pixels.append(px)
print(len(pixels))
mat = np.array(pixels)
mat = np.resize(mat,(256,224))
print(mat)
T = mat.transpose()

print(T)


add 
pop
dec
jp
push
ldax
ldi
inc de
ld bc,20
'''