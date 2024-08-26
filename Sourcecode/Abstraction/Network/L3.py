class L2 :
    def __init__(self):
        self.staticRouting : bool = False
        self.ospfv2 : bool = False
        self.ospfv3 : bool = False
        self.ospfMultiArea : bool = False
        self.ripv1 : bool = False
        self.ripv2 : bool = False
        self.igmpv1 : bool = False
        self.igmpv2 : bool = False
        self.igmpv3 : bool = False
        self.bgpv4 : bool = False
        self.bgpv6 : bool = False
        self.mpbgp : bool = False
        self.loopbackInterfaces : bool = False
        self.vrrp : bool = False
        self.ecmp : bool = False
        self.bfd : bool = False
        self.pbr : bool = False
        self.arp : bool = False
        self.mDNS : bool = False
        self.routeMaps : bool = False
