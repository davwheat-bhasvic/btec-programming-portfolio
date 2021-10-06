from Player import Player
from Deck import Deck
from Card import Card


class Alana(Player):
    def __init__(self, deck: Deck) -> None:
        super().__init__(deck)

    def beginRound(self, deck: Deck) -> None:
        self.getHand().addCard(deck.deal(1)[0])

        pass

    def playRound(self) -> None:
        hand = self.getHand()
        hand.addCard(self._deck.deal(1)[0])  # add second card

        while not self.canStick() and not self.isBust():
            # we need to be able to stick or be bust to continue
            hand.addCard(self._deck.deal(1)[0])

        if self.isBust():
            # we are bust. end the turn
            return

        # We can stick from here, but is it worth it?
        allValues = hand.getNonBustValues()
        playableValues = [value for value in allValues if value >= 17]

        if max(playableValues) >= 20:
            # at this point, sticking is a good idea
            return

        if len(allValues) > 1:
            # we have at least one ace
            minimum = min(allValues)

            while minimum < 17:
                hand.addCard(self._deck.deal(1)[0])
                allValues = hand.getNonBustValues()
                playableValues = [value for value in allValues if value >= 17]
                minimum = min(allValues)

            if self.isBust():
                return

        pass
