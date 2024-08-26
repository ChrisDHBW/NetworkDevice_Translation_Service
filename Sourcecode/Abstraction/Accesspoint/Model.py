from Forschungsarbeit.Service.Abstraction.Physics import Measurements, Environmental
from Forschungsarbeit.Service.Abstraction.Physics import Port
from enum import Enum
class AntennaTypes(Enum):
    Internal = 1
    External = 2
    Directional = 3
    UNKNOWN = 4


class Model :
    def __init__(self):
        self.identifier : str = ""

        self.antennaType : AntennaTypes = None

        self.downlinkPorts : list[Port.Port] = []
        self.uplinkPorts : list[Port.Port] = []

        self.sizes : Measurements.Measurements = None
        self.environmental : Environmental.Environmental = None
        
        self.poeConsumeable : bool = False
        self.requieredClass : int = 0
        self.poeDeliverable : bool = False
        self.deliverableClass : int = 0
        self.canBePoweredByDCVoltage : bool = True
