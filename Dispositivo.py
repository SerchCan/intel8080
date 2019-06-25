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
