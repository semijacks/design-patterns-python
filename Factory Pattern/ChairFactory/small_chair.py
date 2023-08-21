# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Class of Chair"

from interface_chair import IChair


class SmallChair(IChair):
    "The Small Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self.name = "Small Chair"
        self.height = 40
        self.width = 40
        self.depth = 40

    def get_dimensions(self):
        return {
            "name": self.name,
            "width": self.width,
            "depth": self.depth,
            "height": self.height,
        }
