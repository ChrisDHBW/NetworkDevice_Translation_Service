from Forschungsarbeit.Service.Abstraction.Physics import Measurements
from Forschungsarbeit.Service.Abstraction.Physics import Port
from enum import Enum
class Airflows(Enum):
    F2B = 1
    B2F = 2
    UNKNOWN = 3

class ModelTypes(Enum):
    Fixed = 1
    Modular = 2
    UNKNOWN = 3

class Model :
    def __init__(self):
        self.identifier : str = ""

        self.type : ModelTypes = None
        self.airflow : Airflows = None

        self.modulSlots: int = 0

        self.numberOfPowerSupplies : int = 0
        self.numberOfFanTrays : int = 0

        self.downlinkPorts : list[Port.Port] = []
        self.uplinkPorts : list[Port.Port] = []

        self.managementInterface : bool = False

        self.sizes : Measurements.Measurements = None
        
        self.poeDelivery : bool = False
        self.deliveryClass : int = 0
        self.maxDeliveryWattage : int = 0
