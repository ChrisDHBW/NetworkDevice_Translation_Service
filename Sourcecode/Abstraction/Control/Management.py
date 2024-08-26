class Management :
    def __init__(self):
        self.snmpv1 : bool = False
        self.snmpv2 : bool = False
        self.snmpv3 : bool = False
        self.ssh : bool = False
        self.webInterface : bool = False
        self.restApi : bool = False
        self.tools : list[str] = None
