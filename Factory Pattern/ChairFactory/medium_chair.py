# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Class of Chair"

from interface_chair import IChair


class MediumChair(IChair):
    "The Medium Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self.name = "Medium Chair"
        self.height = 60
        self.width = 60
        self.depth = 60

    def get_dimensions(self):
        return {
            "name": self.name,
            "width": self.width,
            "depth": self.depth,
            "height": self.height,
        }
