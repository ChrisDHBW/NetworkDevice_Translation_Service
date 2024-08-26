from Service.Abstraction.Gateways import Scailings
from Forschungsarbeit.Service.Abstraction.Physics import Port, Measurements
from enum import Enum

class UsageTypes(Enum):
    Campus = 1
    Branch = 2
    Hybrid = 3
    UNKNOWN = 4

class Densities(Enum):
    Small = 1
    Medium = 2
    High = 3
    UNKNOWN = 4

class ModelTypes(Enum):
    Fixed = 1
    Modular = 2
    UNKNOWN = 3


class Model :
    def __init__(self):
        self.identifier : str = ""
        
        self.usage : UsageTypes = None
        self.densityClassification : Densities = None

        self.type : ModelTypes = None
        self.numberOfPowerSupplies : int = 0
        self.numberOfFanTrays : int = 0

        self.licenceBasedScailings : bool = False
        self.licences : list[str] = []
        self.scailing : dict[str, dict[str, Scailings.Scailing] | str, Scailings.Scailing | None] = None
        
        self.managementInterface : bool = False

        self.clusterable : bool = False
        self.maxClusterSize : int = 0

        self.ports : list[Port.Port] = []

        self.poeConsumeable : bool = False
        self.requieredClass : int = 0
        self.poeDeliverable : bool = False
        self.deliverableClass : int = 0
        self.canBePoweredByDCVoltage : bool = True

        self.sizes : Measurements.Measurements = None
