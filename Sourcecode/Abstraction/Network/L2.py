class L2 :
    def __init__(self):
        self.vlans : bool = False #802.1q
        self.vlanMaxCount : int = 0
        self.stp : bool = False #802.1s
        self.rstp : bool = False #802.1w
        self.pvst : bool = False
        self.rpvst : bool = False 
        self.mstp : bool = False #802.1s
        self.cdp : bool = False
        self.jumbo : bool = False
        self.qos : bool = False #802.1q
        self.lacp : bool = False #802.3ad
        self.energyEfficientEthernet : bool = False #802.3az
        self.igmpSnooping : bool = False
        self.erps : bool = False
        self.pfc : bool = False
        self.ets : bool = False
        self.dcbx : bool = False
        self.ecn : bool = False
