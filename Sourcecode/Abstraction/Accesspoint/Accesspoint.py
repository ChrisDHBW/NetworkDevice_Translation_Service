from Forschungsarbeit.Service.Abstraction.Network import Security
from Forschungsarbeit.Service.Abstraction.Accesspoints import WirelessProtocols, Radios, Model
from enum import Enum

class EnvironmentTypes(Enum):
    Campus = 1
    Uncovered = 2
    Hospitality = 3
    Remote = 4
    Hardened = 5
    UNKNOWN = 6

class Usages(Enum):
    Indoor = 1
    Outdoor = 2
    UNKNOWN = 3

class RadioTypes(Enum):
    Dual = 1
    Tri = 2
    UNKNOWN = 3

class DensityTypes(Enum):
    Low = 1
    Medium = 2
    High = 3
    Highest = 4
    UNKNOWN = 5

class Accesspoint :
    def __init__(self):
        self.vendor : str = ""
        self.version : str = ""

        self.type : EnvironmentTypes = None
        self.usage : Usages = None

        self.maxSsidsPerRadio : int = 0
        self.maxClientsPerRadio : int = 0

        self.wirelessStandard : str = ""
        self.radioType : RadioTypes = None
        self.densityClassification : DensityTypes = None

        self.tpmModul : bool = False
        self.gpsModul : bool = False

        self.wirelessProtocols : WirelessProtocols.WirelessProtocols = None
        self.security : Security.Security = None
        self.radios : Radios.Radios = None

        self.operatingSystems : list[str] = []

        self.models : list[Model.Model] = []
        
        
