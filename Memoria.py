class Memory:
    def __init__(self, TAMMEM=2**16):
        self.size = TAMMEM
        self.Memory = []
        for i in range(TAMMEM):
            self.Memory.append(0xff)

    def getMemory(self, PC):
        return self.Memory[PC%self.getSize()]

    def getScreenMemory(self):
        return self.Memory[0x2400:0x4000]

    def getSize(self):
        return self.size

    def setMemory(self, PC, value):
        #if PC >= 0x2000 and PC <= 0x3fff:
        self.Memory[PC%self.getSize()] = value

    def Write(self, file):
        with open(file, "w") as openFile:
            for value in self.Memory:
                hexValue = hex(int(value))
                openFile.write(str(hexValue)+" ")

    def Load(self, file):
        i = 0
        with open(file, "br+") as openFile:
            for line in openFile:
                for c in line:
                    # print(str(c))
                    self.Memory[i] = int(c)
                    i += 1

    def doChecksum(self,data):
        print(data)
    def LoadHex(self,file):  #intelHEX
        with open(file,'r+') as F:
            for line in F.readlines():
                if line[0] == ':':
                    byteCount = int("0x"+line[1:3],16)
                    address = int("0x"+line[7:3:-1][::-1],16)
                    record = int(line[7:9],16)
                    # check = doChecksum([byteCount,address,record,data])
                    i=0
                    while i < byteCount:
                        print(address)
                        data = int(line[10+i]+line[11+i],16)
                        self.setMemory(address+i,data)
                        i+=2
                    CheckSum = int(line[-1:-3:-1],16)
                else:
                    print("Error: Unknown Format")
#pantalla esquina sup izq y de izq a derecha
# la pantalla se voltea 90 grados
#walkofmind.com/programming/side/hardware.htm

if __name__ == "__main__":
    memory = Memory()
    # Escrituras

    #memory.setMemory(2, 14)
    #memory.setMemory(3, 16)
    # memory.Write("file.bin")
    # Lecturas
    #memory.Load("invaders.rom")
    
    memory.LoadHex('file.hex')
    memory.Write('newFileCPU')
