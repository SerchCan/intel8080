class Banderas:
    def __init__(self):
        self.flagNames = ["Z", "S", "C", "P", "A"]
        self.flags = {}
        for flag in self.flagNames:
            self.flags[flag] = False

    def setFlag(self, flag, value):
        self.flags[flag.upper()] = value

    def getFlag(self, flag):
        return self.flags[flag.upper()]

    def getPSWRegister(self):
        order = ['S', 'Z', 0, 'A', 0, 'P', 1, 'C']
        bit = 7

        res = 0
        for value in order:
            if value != 0 and value != 1:
                res += self.getFlag(value) << bit
            else:
                res += value << bit
            bit -= 1
        return res

    def setPSWRegister(self, values):
        order = ['S', 'Z', 0, 'A', 0, 'P', 1, 'C']
        for i, val in enumerate(values):
            if(order[i] != 0 and order[i] != 1):
                self.setFlag(order[i], int(val))

    def displayFlags(self):
        print("PSW: ", end="")
        endler = " "
        last = (len(self.flagNames)-1)
        for i, f in enumerate(self.flagNames):
            if i == last:
                endler = "\n"
            if self.flags[f]:
                print(f, end=endler)
            else:
                print("-", end=endler)


if __name__ == "__main__":
    b = Banderas()
    b.setFlag("C", 1)
    b.setFlag("z", 1)
    b.displayFlags()

    print(b.getPSWRegister())
