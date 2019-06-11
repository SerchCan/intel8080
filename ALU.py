from Banderas import Banderas


class ALU:
    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.flags = Banderas()

    def displayFlags(self):
        self.flags.displayFlags()

    def setOP1(self, value):
        self.op1 = value

    def setOP2(self, value):
        self.op2 = value

    def updateFlags(self,res):
        if res == 0:
            self.flags.setFlag("Z", True)
        else:
            self.flags.setFlag("Z", False)
        if (res & 0x80) == 0x80:
            self.flags.setFlag("S", True)
        else:
            self.flags.setFlag("S", False)
        self.checkParity(res)
    
    def checkParity(self,res):
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
        self.flags.setFlag("Z",False)
        self.flags.setFlag("S",False)
        self.flags.setFlag("C",False)
        self.flags.setFlag("P",False)
        self.flags.setFlag("A",False)
        res= ~self.op1
        return res

    def SUB(self):
        pass
    

    def BCD(self):
        #value is int so...
        digits = str(self.op1)
        bcds=[]
        for d in digits:
            binary = bin(int(d))
            bcds.append(int(binary,2))
        print("bcds",bcds)
        res = (bcds[0]<<4) | bcds[1]

        if(res > 0x0f):
            self.flags.setFlag("A", True)
        else:
            self.flags.setFlag("A", False)
        if(res > 255):
            res = res & 0xff
            self.flags.setFlag("C", True)
        else:
            self.flags.setFlag("C", False)
        self.updateFlags(res)
        return res
    
    def RLC(self):
        A = self.op1
        A = A<<1
        carry = (A & 0x100)>>8
        A = A&0xff
        A = A | carry
        self.flags.setFlag("C",carry)
        return  A

    def RRC(self):
        A = self.op1
        carry = (A&0x01)<<7
        A = A>>1
        A = A | carry
        self.flags.setFlag("C",carry)
        return  A

    #4 5 6 7
if __name__ == "__main__":
    alu = ALU()
    alu.setOP1(14)
    alu.setOP2(6)

    print("AND", alu.AND())
    alu.flags.displayFlags()
    print("OR",alu.OR())
    alu.flags.displayFlags()
    print("XOR",alu.XOR())
    alu.flags.displayFlags()
    print("NOT",alu.NOT())
    alu.flags.displayFlags()
    print("ADD:", alu.ADD())
    alu.flags.displayFlags()

    print("BCD", alu.BCD())
    alu.flags.displayFlags()

    print("RLC",hex(alu.RLC()))
    alu.flags.displayFlags()
    
    print("RLC",hex(alu.RRC()))
    alu.flags.displayFlags()

