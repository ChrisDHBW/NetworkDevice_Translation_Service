from enum import Enum

class StackingProtocols(Enum):
    VSF = 1
    VSX = 2
    Backplane = 3
    NotCapable = 4
    UNKNOWN = 5

class Stacking :
    def __init__(self):
        self.type : StackingProtocols = None
        self.maxStackingMembers : int = 0
