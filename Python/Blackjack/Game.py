class Game:
    def __init__(self) -> None:
        pass

    def printWelcomeMessage(self) -> None:
        print("Welcome to Blackjack!")
        print("")
        print("You'll be playing against the AI Dealer, Alana.")
        print("")
        print("Basic rules:")
        print("1. You are dealt two cards from a shuffled deck")
        print("2. You should aim to get as close to 21 as possible")
        print(
            "3. If your hand value exceeds 21 (22+), you are 'bust' and lose the round"
        )
        print(
            "4. Number cards are worth their face value, picture cards are worth 10 and Aces can be either 1 or 11"
        )
        print(
            "5. During your turn, you can 'Twist' to draw another card, or 'Stick' to end your turn"
        )
        print(
            "6. In order to stick, you must have at least 2 cards, and your hand must be worth 17 or higher"
        )
        print("7. You win if your hand is valued above that of the Dealer, Alana")
        print("8. You lose if your hand is valued below that of the Dealer, Alana")
        print("9. You win if the Dealer, Alana, is bust")
        print("")
        print("")
        print("Press ENTER to start...")
        input()