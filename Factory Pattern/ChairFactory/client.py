"Create Chair Client"

from chair_factory import ChairFactory

CHAIR = ChairFactory().get_chair("medium")
print(CHAIR.get_dimensions())

CHAIR = ChairFactory().get_chair("small")
print(CHAIR.get_dimensions())

CHAIR = ChairFactory().get_chair("big")
print(CHAIR.get_dimensions())
