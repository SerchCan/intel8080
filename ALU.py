from Banderas import Banderas


class ALU:
    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.flags = Banderas()

    def getFlags(self):
        return self.flags

    def displayFlags(self):
        self.flags.displayFlags()

    def setOP1(self, value):
        self.op1 = value

    def setOP2(self, value):
        self.op2 = value

    def updateFlags(self, res):
        if res == 0:
            self.flags.setFlag("Z", True)
        else:
            self.flags.setFlag("Z", False)
        if (res & 0x80) == 0x80:
            self.flags.setFlag("S", True)
        else:
            self.flags.setFlag("S", False)
        self.checkParity(res)

    def checkParity(self, res):
        # Parity
        count = 0
        for i in bin(res):
            if i == "1":
                count += 1
        if(count % 2 == 0):
            self.flags.setFlag("P", False)
        else:
            self.flags.setFlag("P", True)

    def ADD(self):
        temp1 = self.op1 & 0x0f
        temp2 = self.op2 & 0x0f
        res = temp1+temp2

        if(res > 0x0f):
            self.flags.setFlag("A", True)
        else:
            self.flags.setFlag("A", False)

        temp1 = self.op1 & 0xf0
        temp2 = self.op2 & 0xf0
        res += temp1+temp2

        if(res > 255):
            res = res & 0xff
            self.flags.setFlag("C", True)
        else:
            self.flags.setFlag("C", False)

        self.updateFlags(res)
        return res

    def AND(self):
        res = self.op1 & self.op2
        self.flags.setFlag("C", False)
        self.flags.setFlag("A", False)
        self.updateFlags(res)
        return res

    def OR(self):
        res = self.op1 | self.op2
        self.flags.setFlag("C", False)
        self.flags.setFlag("A", False)
        self.updateFlags(res)
        return res

    def XOR(self):
        res = self.op1 ^ self.op2
        self.flags.setFlag("C", False)
        self.flags.setFlag("A", False)
        self.updateFlags(res)
        return res

    def NOT(self):
        #Z, S, C, P, A
        self.flags.setFlag("Z", False)
        self.flags.setFlag("S", False)
        self.flags.setFlag("C", False)
        self.flags.setFlag("P", False)
        self.flags.setFlag("A", False)
        res = ~self.op1
        return res

    def SUB(self):
        cin=0
        v1 = self.op1 & 0x0f
        v2 = self.op2 & 0x0f
        r = v1-v2 - cin
        if r > 15:
            self.flags.setFlag("A", True)
        else:
            self.flags.setFlag("A", True)

        out = self.op1 - self.op2 - cin
        self.updateFlags(out)
        return out & 0x00ff
        '''    CO
        0-0=0
        0-1=1  1
        1-0=1
        1-1=0

        e1  e2  cin |cout    s
        0   0   0   0   0
        0   0   1   1   1
        0   1   0   1   1
        0   1   1   1   0
        1   0   0   0   1
        1   0   1   0   0
        1   1   0   0   0
        1   1   1   1   1

        e1,e2
        r

        for e1 in range 255:
            for e2 in range 255
                r := e1-e2 complemento 2
        '''
    # fill in 0 with bits 01 -> 0001
    def leftFilled(self,value):
        n = 0
        t = ""
        while (len(value)+n) % 4 != 0:
            t += "0"
            n += 1
        return t+value
    def BCD(self):
        # value is int so...
        digits = str(self.op1)
        bcds = ""
        for d in digits:
            binary = self.leftFilled(bin(int(d))[2:])
            bcds += binary

        res = int(bcds, 2)

        if(res > 0x0f):
            self.flags.setFlag("A", True)
        else:
            self.flags.setFlag("A", False)
        temp  = res&0xf0
        if(temp > 255):
            res = res & 0xff
            self.flags.setFlag("C", True)
        else:
            self.flags.setFlag("C", False)
        self.updateFlags(res)
        return res

    def RLC(self):
        A = self.op1
        A = A << 1
        carry = (A & 0x100) >> 8
        A = A & 0xff
        A = A | carry
        self.flags.setFlag("C", carry)
        return A

    def RRC(self):
        A = self.op1
        carry = (A & 0x01) << 7
        A = A >> 1
        A = A | carry
        self.flags.setFlag("C", carry)
        return A

    def doMemoryPair(self):
        H = self.op1
        L = self.op2
        return (H << 4) | L

    def INX(self, isPair=True):
        pair = 0
        if isPair == True:
            pair = self.doMemoryPair()
        else:
            pair = self.op1
        pair += 1
        return pair

    def DCX(self, isPair=True):
        pair = 0
        if isPair == True:
            pair = self.doMemoryPair()
        else:
            pair = self.op1
        pair -= 1
        return pair

    # 4 5 6 7
if __name__ == "__main__":
    alu = ALU()

    alu.setOP1(25)
    alu.setOP2(5)
    print("AND", alu.AND())
    alu.flags.displayFlags()
    print("OR", alu.OR())
    alu.flags.displayFlags()
    print("XOR", alu.XOR())
    alu.flags.displayFlags()
    print("NOT", alu.NOT())
    alu.flags.displayFlags()
    print("ADD:", alu.ADD())
    alu.flags.displayFlags()
    print("SUB:", alu.SUB())
    alu.flags.displayFlags()
    print("BCD", alu.BCD())
    alu.flags.displayFlags()

    print("RLC", hex(alu.RLC()))
    alu.flags.displayFlags()

    print("RRC", hex(alu.RRC()))
    alu.flags.displayFlags()