from Card import Card


class Hand:
    def __init__(self) -> None:
        self.cards = []
        pass

    def addCard(self, card: Card) -> None:
        self.addCards([card])
        pass

    def addCards(self, cards: list[Card]) -> None:
        self.cards.extend(cards)
        pass

    def getNonBustValues(self) -> list[int]:
        values = self.getAllValues()

        return [value for value in values if value <= 21]

    def getAllValues(self) -> list[int]:
        values = self._calculateValue([0], self.cards)

        return values

    def _calculateValue(self, values: list[int], cards: list[Card]) -> list[int]:
        if len(cards) == 0:
            return values

        currentCard = cards.pop()
        newValues = []

        cardValues = currentCard.getValues()

        for cardVal in cardValues:
            for value in values:
                newValues.append(value + cardVal)

        return self._calculateValue(newValues, cards)