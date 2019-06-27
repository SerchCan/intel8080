class Device():
    def __init__(self):
        self.value = 0

    def setDevice(self, value):
        self.value = value

    def getDevice(self):
        return self.value


class IDevice(Device):
    def __init__(self):
        super().__init__()


class ODevice(Device):
    def __init__(self):
        super().__init__()


class IODevice(IDevice, ODevice):
    pass


if __name__ == "__main__":
    IO = IODevice()
    print(IO.getDevice())

#tarjeta de video dispositivo, Memoria de salida
#24ff 3fff
'''
procedude

for addr 2400 3fff:

    byte= memoryGet(m,addr)
    for i=7 to 0: #bits
        p = (byte >> i) & 0x01
        pixelloation screen,
'''
    

