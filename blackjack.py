import random


class values:
    @classmethod
    def findAceValue(cls, totalValue):
        if totalValue + 11 > 21:
            return 1
        else:
            return 11

    @classmethod
    def canContinue(cls, totalValue):
        if totalValue > 21:
            return False
        else:
            return True
