from Forschungsarbeit.Service.Abstraction.Control import Management
from Forschungsarbeit.Service.Abstraction.Network import Security
from Forschungsarbeit.Service.Abstraction.Network import L2, L3, L4, L7
from Forschungsarbeit.Service.Abstraction.Switches import Model, Modul, VendorSpecificFeatures
from enum import Enum

class ChassisTypes(Enum):
    Fixed = 1
    Modular = 2
    UNKNOWN = 3

class Switch :
    def __init__(self):
        self.vendor : str = ""
        self.version : str = ""

        self.layer : int = 0
        self.chassisType : ChassisTypes = None

        self.managed : bool = False

        self.l2 : L2 = None
        self.l3 : L3 = None
        self.l4 : L4 = None
        self.l7 : L7 = None
        self.security : Security = None
        self.management : Management = None

        self.operatingSystems : list[str] = []

        self.vendorSpecificFeatures : VendorSpecificFeatures = None
        
        self.models : list[Model.Model] = None
        self.moduls : list[Modul.Modul] = None
