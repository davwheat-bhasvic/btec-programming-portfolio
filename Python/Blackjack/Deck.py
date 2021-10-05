from Card import Card
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self._buildDeck()

        pass

    def deal(self, count: int) -> list[Card]:
        cards = []

        for _ in range(count):
            card = self.cards.pop(0)
            cards.append(card)
            self.cards.append(card)

        return cards

    def _buildDeck(self) -> None:
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1, 14):
                displayName = str(rank)

                if rank == 1:
                    displayName = "A"

                if rank > 10:  # Picture cards
                    displayName = ["J", "Q", "K"][rank - 11]

                self.cards.append(Card(suit, rank, displayName))

        self.shuffle()

        pass

    def shuffle(self) -> None:
        shuffle(self.cards)

        pass
