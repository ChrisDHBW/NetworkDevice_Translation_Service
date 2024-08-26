from Forschungsarbeit.Service.Abstraction.Network import Security
from Forschungsarbeit.Service.Abstraction.Gateways import Model
from enum import Enum

class GatewayTypes(Enum):
    Campus = 1
    Branch = 2
    Hybrid = 3
    UNKNOWN = 4

class Gateway :
    def __init__(self):
        self.vendor : str = ""
        self.version : str = ""
        self.type : GatewayTypes = None
        self.tpmModul : bool = False
        self.security : Security.Security = None
        self.operatingSystems : list[str] = []
        self.models : list[Model.Model] = []
