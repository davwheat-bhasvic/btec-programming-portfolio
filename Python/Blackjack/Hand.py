from Card import Card


class Hand:
    def __init__(self) -> None:
        self.cards = []
        pass

    def addCard(self, card: Card) -> None:
        self.cards.append(card)
        pass

    def getAllValues() -> list[int]:
        pass

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