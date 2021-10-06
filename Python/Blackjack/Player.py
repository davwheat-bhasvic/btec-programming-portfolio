from Deck import Deck
from Hand import Hand
from Card import Card


class Player:
    def __init__(self, deck: Deck) -> None:
        self._hand = Hand()
        self._deck = deck
        pass

    def getHand(self) -> Hand:
        return self._hand

    def isBust(self) -> bool:
        values = self.getHand().getNonBustValues()
        return len(values) == 0

    def getCardCount(self) -> int:
        return len(self._hand.cards)

    def canStick(self) -> bool:
        if self.getCardCount() < 2:
            return False

        if self.isBust():
            return False

        if max(self.getHand().getNonBustValues()) < 17:
            return False

        return True
