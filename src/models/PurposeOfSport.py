from enum import Enum, unique


@unique
class PurposeOfSport(Enum):
    WELLNESS = 1
    REHABILITATION = 2
    COMPETITION = 3
