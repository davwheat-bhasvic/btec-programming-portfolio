class Card:
    def __init__(self, suit, rank, displayName) -> None:
        self.suit = suit
        self.rank = rank
        self.displayName = displayName

    def getValues(self) -> list[int]:
        if self.rank == 1:  # Ace
            return [1, 11]

        if self.rank > 10:  # J, Q, K
            return [10]

        return [self.rank]
