#  Mini Project - Rock Paper Scissors
import random
class Game:
    def __init__(self, ):
        self.items = ["r","p","s"]
    def get_user_item(self):
        while True:
            user_item = input("Select (r)ock, (p)aper, or (s)cissors: ")
            if user_item.lower() in self.items:
                return user_item.lower()
            else:
                print("Invalid choice. Please try again.")
    def get_computer_item(self):
        return random.choice(self.items)
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "r" and computer_item == "s") or \
             (user_item == "p" and computer_item == "r") or \
             (user_item == "s" and computer_item == "p"):
            return "win"
        else:
            return "lose"
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You chose: {user_item}. The computer chose: {computer_item}.  Result: {result}")
        return result