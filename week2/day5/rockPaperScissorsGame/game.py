import random

class Game:
    def get_user_item(self):
        user_item = input("Please choose your move: rock, paper or scissors? ")
        return user_item
    
    def get_computer_item(self):
        rand = random.randint(1,3)
        if rand == 1:
            return "rock"
        elif rand == 2:
            return "paper"
        else:
            return "scissors"
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:         #we take care of the more specific case, the "global" one
            return "We have a tie"
        
        if user_item == "rock":                #nested ifs because each if block is independent from the other
            if computer_item == "scissors":
                return "You win!"
            else:
                return "You lose!"
        
        if user_item == "paper":
            if computer_item == "rock":
                return "You win!"
            else:
                return "You lose!"
        
        if user_item == "scissors":
            if computer_item == "paper":
                return "You win!"
            else:
                return "You lose!"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)
        print(user_item)
        print(computer_item)
        print(game_result)       # return the result so main() in rock-paper-scissors.py can use it


game1 = Game()
result = game1.play()        # play() is a method, so you need to CALL IT WITH PARENTHESES to execute it 





