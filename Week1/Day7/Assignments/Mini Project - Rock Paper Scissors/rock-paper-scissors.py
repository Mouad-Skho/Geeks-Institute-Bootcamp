from game import Game
def get_user_menu_choice():
    print('''
    Welcome to Rock Paper Scissors!

    What would you like to do?

    (p) Play a new game
    (s) Show scores
    (q) Quit
    '''
    )
    choice = input("Enter your choice: ").lower()
    if choice in ("p", "s", "q"):
        return choice
    print("Invalid choice.")
    return None
def print_results(results):
    print(f'''
    Game Results:
    You won {results["win"]} times
    You lose {results["lose"]} times
    You draw {results["draw"]} times

    Thank you for playing!
''')
def main():
    results = {"win": 0, "lose": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "q":
            print_results(results)
            break
        elif choice == "p":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "s":
            print_results(results)



main()