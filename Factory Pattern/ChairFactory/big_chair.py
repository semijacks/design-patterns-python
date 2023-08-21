# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Class of Chair"

from interface_chair import IChair


class BigChair(IChair):
    "The  Big Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self.name = "Big Chair"
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {
            "name": self.name,
            "width": self.width,
            "depth": self.depth,
            "height": self.height,
        }
