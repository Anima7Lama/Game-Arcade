import random
import time
import statistics

# Helper function to calculate and display statistics
def display_statistics(times):
    if times:
        #Display statistics if there are recorded times
        print(f"\n--- Game Statistics ---")
        print(f"Minimum Time: {min(times):.2f} seconds")
        print(f"Maximum Time: {max(times):.2f} seconds")
        print(f"Mean Time: {statistics.mean(times):.2f} seconds")
        print(f"Median Time: {statistics.median(times):.2f} seconds")
        #checking if there are more than one recorded times in times list
        if len(times) > 1:
            print(f"Standard Deviation: {statistics.stdev(times):.2f} seconds")
        print("------------------------\n")
    else:
        # if no times recorded
        print("No data to display statistics.\n")

# Game 1: Word Scramble
def word_scramble_game():
    #list of words for the game
    words = ["python", "statistics", "arcade", "fun", "education"]
    times = []
    #Iterating through each word in the list
    for word in words:
        #scrambling the word
        scrambled = list(word)
        random.shuffle(scrambled)
        scrambled = ''.join(scrambled)
        #Displaying scrambled word
        print(f"Unscramble the word: {scrambled}")
        
        start_time = time.time() #Recording start time
        #Player's guess
        guess = input("Your guess: ")
        #Recording end time
        end_time = time.time()
        #Calculating and recording time taken
        times.append(end_time - start_time)
        #Checking if guess is correct
        if guess == word:
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct word was {word}.\n")
    #calling the function to display statistics for the game
    display_statistics(times)

# Game 2: Tic Tac Toe
def tic_tac_toe_game():
    print("======================")
    print("Welcome to Tic Tac Toe")
    print("======================")

    # Initialize game board as a dictionary
    gameBoard = {1: '1', 2: '2', 3: '3',
                 4: '4', 5: '5', 6: '6',
                 7: '7', 8: '8', 9: '9'}

    #function to print the game board
    def printGameBoard():
        print("\n+---+---+---+")
        for i in range(3):
            print(f"| {gameBoard[1+i*3]} | {gameBoard[2+i*3]} | {gameBoard[3+i*3]} |")
            print("+---+---+---+")

    # Modify game board based on player/computer move
    def modifyGameBoard(num, turn):
        gameBoard[num] = turn

    # Decide the winner based on current game board
    def decideWinner(gameBoard):
        winningPatterns = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
                           (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
                           (1, 5, 9), (3, 5, 7)]             # Diagonals
        for pattern in winningPatterns:
            if gameBoard[pattern[0]] == gameBoard[pattern[1]] == gameBoard[pattern[2]]:
                return gameBoard[pattern[0]]
        return None

    # Main game loop
    exitLoop = False
    turnCounter = 0 #number of turns played

    #loops until the game ends
    while not exitLoop:
        # Player's turn if turnCounter is even
        if turnCounter % 2 == 0:
            printGameBoard()
            try:
                numberPicked = int(input("\nChoose a number from 1 to 9: "))                
                #checking if the number picked is within the valid range and whether the corresponding cell is occupied or not
                if numberPicked in range(1, 10) and gameBoard[numberPicked] != 'X' and gameBoard[numberPicked] != 'O':
                    modifyGameBoard(numberPicked, 'X')
                    turnCounter += 1
                else:
                    print("Invalid input! Please choose an available position.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        # Computer's turn if turnCounter is odd
        else:
            #Iterates over each key(position) of the board and randomly chooses any one available position
            compChoice = random.choice([num for num in gameBoard.keys() if gameBoard[num] != 'X' and gameBoard[num] != 'O'])
            modifyGameBoard(compChoice, 'O')
            turnCounter += 1
    
        # Check for winner or draw
        winner = decideWinner(gameBoard)
        if winner:
            printGameBoard()
            if winner == 'X':
                print("Congratulations! You have won!\n")
            else:
                print("You lost! The computer has won!\n")
            exitLoop = True
        elif turnCounter == 9:
            printGameBoard()
            print("It's a draw!")
            exitLoop = True

# Game 3: Math Quiz
def math_quiz_game():
    # List of mathematical operations for the game
    operations = ['+', '-', '*', '/']
    times = []
    correct_answers = 0
    #Iterating through 5 questions
    for i in range(5):
        # Generating random numbers and operation
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(operations)
        question = f"{num1} {operation} {num2}"
        #eval function calculates the generated expression
        answer = eval(question)
        print(f"Solve: {question}")
        start_time = time.time()
        try:
            guess = float(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  # Skips the rest of the loop iteration if input is invalid
        end_time = time.time()
        times.append(end_time - start_time)
        #checking if the answer is correct
        if abs(guess - answer) < 0.01:
            correct_answers += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer was {answer}.\n")
    #Displaying total correct answers and statistics for the game
    print(f"You got {correct_answers} out of 5 questions correct.")
    display_statistics(times)

# Game 4: Hangman
def hangman_game():
    #list of words for the game
    words = ["python", "statistics", "arcade", "fun", "education"]
    word = random.choice(words)
    
    #storing "_" in guessed variable according to the length of the word
    guessed = ['_'] * len(word)
    times = []
    wrong_attempts = 0
    print("Welcome to Hangman!")
    
    # Loops until word is guessed or wrong attempts exceeds 6 times
    while ''.join(guessed) != word and wrong_attempts < 6:
        #Displays current state of word
        print(f"Word: {' '.join(guessed)}")
        #Player's guess
        letter = input("Guess a letter: ")
        start_time = time.time()
        #Checks if letter is in word
        if letter in word:
            #if the guessed letter is in the word, reveal it in guessed word
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            #If the guessed letter is not in the word, increment wrong attempt
            wrong_attempts += 1
        #Displays remaining wrong attempts
        print(f"Wrong attempts: {wrong_attempts}/6\n")
    #Displays game result and statistics
    if ''.join(guessed) == word:
        end_time = time.time()
        times.append(end_time - start_time)
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"You lost. The word was: {word}")
    display_statistics(times)

# Main Arcade Menu
def arcade_menu():
    #Loops until player chooses to exit
    while True:
        print("Welcome to the Arcade!")
        print("1. Word Scramble")
        print("2. Tic Tac Toe")
        print("3. Math Quiz")
        print("4. Hangman")
        print("5. Exit")
        choice = input("Select a game (1-5): ")
        if choice == '1':
            word_scramble_game()
        elif choice == '2':
            tic_tac_toe_game()
        elif choice == '3':
            math_quiz_game()
        elif choice == '4':
            hangman_game()
        elif choice == '5':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

# Run the Arcade
arcade_menu()
