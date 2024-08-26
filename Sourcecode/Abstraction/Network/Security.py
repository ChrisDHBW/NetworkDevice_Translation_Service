class Security :
    def __init__(self):
        self.radius : bool = False
        self.tacacs : bool = False
        self.tacacsPlus : bool = False
        self.macAuth : bool = False
        self.dotOneXAuth : bool = False
        self.dotOneXSupplicant : bool = False
        self.aclsv4 : bool = False
        self.aclsv6 : bool = False
        self.captivePortals : bool = False
        self.stpRootGuard : bool = False
        self.stpBPDUGuard : bool = False
        self.arpInspection : bool = False
