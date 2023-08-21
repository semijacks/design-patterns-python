# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Factory Class"

from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair


class ChairFactory:
    "The Factory Class"

    @staticmethod
    def get_chair(chair):
        "A static method to get a chair"
        if chair == "small":
            return SmallChair()
        if chair == "medium":
            return MediumChair()
        if chair == "big":
            return BigChair()
        return None
