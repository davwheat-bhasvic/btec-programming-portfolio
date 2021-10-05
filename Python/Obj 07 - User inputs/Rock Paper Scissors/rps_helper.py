from random import choice

class RPS_Game:
    def __init__(self):
        self.score = { 'player': 0, 'computer': 0 }
        self.history = []
        self.possible_plays = ['Rock', 'Paper', 'Scissors']


    def increment_player_score(self):
        self.score.update({'player': self.score.get('player') + 1})


    def increment_computer_score(self):
        self.score.update({'computer': self.score.get('computer') + 1})

    
    def get_player_score(self):
        return self.score.get('player')

    
    def get_computer_score(self):
        return self.score.get('computer')


    def generate_play(self):
        return choice(self.possible_plays)


    def determine_round_winner(self, player, computer):
        pResp = player.lower()
        cResp = computer.lower()

        self.history.append({'player': pResp, 'computer': cResp})

        if (pResp == "rock" and cResp != "paper"):
            self.increment_player_score()
            return "player"
        elif (pResp == "paper" and cResp != "scissors"):
            self.increment_player_score()
            return "player"
        elif (pResp == "scissors" and cResp != "rock"):
            self.increment_player_score()
            return "player"
        else:
            self.increment_computer_score()
            return "computer"


    def interpret_input(self, inp):
        i = inp.lower()

        if (i in ["rock", "r"]):
            return "Rock"
        elif (i in ["paper", "p"]):
            return "Paper"
        elif (i in ["scissors", "s"]):
            return "Scissors"
        else:
            raise ValueError("Invalid player input")

    
    def start_round(self):
        print(f"\nRound {len(self.history) + 1}!")

        valid = False
        playerChoice = ""

        while not valid:
            playerChoice = input("Choose your play: (r/p/s) ")

            try:
                playerChoice = self.interpret_input(playerChoice)
                valid = True
            except ValueError:
                # not needed, but helps with code clarity
                valid = False
                print("\nThat's not a valid input. Try again.")
        
        computerResponse = self.generate_play()

        winner = self.determine_round_winner(playerChoice, computerResponse)
        
        if (winner == "player"):
            print(f"\nYou won! The computer chose {computerResponse}.")
        else:
            print(f"\nOh no, you lost! The computer chose {computerResponse}.")
