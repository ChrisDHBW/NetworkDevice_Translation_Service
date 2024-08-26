from Forschungsarbeit.Service.Abstraction.Physics import Measurements
from Forschungsarbeit.Service.Abstraction.Physics import Port
from enum import Enum
class ModulTypes(Enum):
    Access = 1
    CoreAgg = 2
    Uplink = 3
    Stacking = 4
    UNKNOWN = 5

class Modul :
    def __init__(self):
        self.identifier : str = ""
        self.type : ModulTypes = None
        self.downlinkPorts : list[Port.Port] = []
        self.uplinkPorts : list[Port.Port] = []
        self.poeDelivery : bool = False
        self.deliveryClass : int = 0
        self.maxDeliveryWattage : int = 0
