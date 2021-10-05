from rps_helper import RPS_Game

current_game = None
round_count = 10


def begin_game():
    current_game = RPS_Game()
    print("Welcome to Rock Paper Scissors!")
    print(
        "\nYou'll be competing against the AI (computer) to win one of hundreds of non-existant prizes. Woohoo"
    )
    print(
        "\nThe computer doesn't know what you've picked (well obviously it does, otherwise it couldn't work out who won, but it doesn't pick based on that)."
    )

    while True:
        current_game.start_round()

        p_score = current_game.get_player_score()
        c_score = current_game.get_computer_score()

        if p_score >= 10 or c_score >= 10:
            break

    print("\nThe game is over!")
    print("The final score was:")
    print(f"Player   - {p_score}")
    print(f"Computer - {c_score}")

    if p_score > c_score:
        print("\nYou won!")
    elif p_score < c_score:
        print("\nYou lost.")
    else:
        print("\nYou drew.")


begin_game()