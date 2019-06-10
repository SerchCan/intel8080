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
    print(b.getFlag("C"))
    b.displayFlags()
