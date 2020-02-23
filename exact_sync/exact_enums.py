from enum import Enum

class VECTOR_TYPE(Enum):
    BOUNDING_BOX = 1
    POINT = 2
    LINE = 3
    MULTI_LINE = 4
    POLYGON = 5
    FIXED_SIZE_BOUNDING_BOX = 6