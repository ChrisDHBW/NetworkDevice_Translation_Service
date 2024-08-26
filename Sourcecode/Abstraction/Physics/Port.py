class Port :
    def __init__(self):
        self.type : str = ""
        self.macSecPorts : bool = False
        self.macSecMaxSpeed : int = 0
        self.poeDelivery : bool = False
        self.poeDeliveryClass : int = 0
        self.canConsumePoE : bool = False
        self.poeConsumeClass : int = 0
        self.speeds : list[int] = [] # Value in MBits
