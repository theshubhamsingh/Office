# Project 1: Game Collection 📂

Read before you run this program on your computer.

## Prerequisites 

Before running the games, ensure you have the following installed on your computer:

- **Python 3.x**: You can download it from the [official Python website](https://www.python.org/downloads/).
- **Code Editor or IDE**: (e.g., VSCode, PyCharm) for editing and running the script.
- **Git (optional)**: For cloning the repository if you are using version control.

## Installation 💿

1. **Clone the repository (if using Git):**
    ```sh
    git clone https://github.com/theshubhamsingh/Office/
    cd Office
    ```

2. **Navigate to the project directory:**
    ```sh
    cd /Users/sam/Documents/Code/Python/Office/Project1
    ```

3. **Install any required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Available Games 🎮

1. **Rock, Paper, Scissors**
2. **Advanced Quiz Game**
3. **Simple Quiz Game**
4. **Guess the Number**

---

### Rock, Paper, Scissors ✂️🪨📃

A classic hand game played between two players, in this case, the player and the computer.

#### How It Works

1. **Player Input**:
    - The player chooses one of the three options: Rock, Paper, or Scissors.
    - The input is case-insensitive and validated to ensure it is one of the allowed options.

2. **Computer Choice**:
    - The computer randomly selects one of the three options using the `random.choice()` function.

3. **Determine the Winner**:
    - The game compares the player's choice and the computer's choice:
      - Rock beats Scissors.
      - Scissors beats Paper.
      - Paper beats Rock.
    - If both choices are the same, it results in a tie.

4. **Feedback**:
    - The game provides feedback on the result of each round:
      - `"You win!"` if the player wins.
      - `"You lose!"` if the computer wins.
      - `"It's a tie!"` if both choices are the same.

5. **Loop**:
    - The game can continue for multiple rounds based on the player's preference.

#### Optional Enhancements

1. **Score Tracking**:
    - Keep track of the number of wins, losses, and ties.

2. **Best of Series**:
    - Allow the player to play a best of 3, 5, or 7 series.

3. **Enhanced User Interface**:
    - Add a graphical user interface (GUI) for a more interactive experience.

4. **Play Again Option**:
    - Allow the player to play multiple rounds without restarting the program.

---

### Simple Quiz Game 🕹️

A straightforward quiz game where the player answers multiple-choice questions.

#### How It Works

1. **Question Presentation**:
    - The game presents a series of questions to the player, each with multiple-choice answers.
    - Each question is displayed one at a time.

2. **Player Input**:
    - The player selects an answer from the provided options.
    - The input is validated to ensure it matches one of the available choices.

3. **Feedback**:
    - The game provides immediate feedback on whether the selected answer is correct or incorrect.
    - It keeps track of the player's score based on the number of correct answers.

4. **Score Display**:
    - At the end of the quiz, the game displays the player's total score and the number of correct answers.

5. **Loop**:
    - The game can be designed to allow multiple rounds of quizzes based on the player's preference.

#### Optional Enhancements

1. **Add More Questions**:
    - Increase the number of questions to make the quiz more challenging.

2. **Categorize Questions**:
    - Group questions into categories (e.g., Science, History, Sports) and allow the player to choose a category.

3. **Track High Scores**:
    - Save the highest scores in a file and display the top scores.

4. **Timed Quiz**:
    - Add a timer for each question to increase the difficulty level.

5. **Randomize Questions**:
    - Randomly select questions from a larger pool to ensure a different quiz each time.

---

### Guess the Number 🎲

A simple, text-based game where the computer generates a random number, and the player tries to guess it.

#### How It Works

1. **Random Number Generation**:
   - The program generates a random number between 1 and 100 using the `random.randint()` function.

2. **Player Input**:
   - The player enters their guess, which is converted to an integer. 
   - If the input is invalid (e.g., not a number), it catches the error and asks again.

3. **Feedback**:
   - The game provides feedback:
     - `"Too low!"` if the guess is less than the number.
     - `"Too high!"` if the guess is greater than the number.
     - `"Congratulations!"` if the player guesses correctly.

4. **Loop**:
   - The game continues in a loop until the correct number is guessed.

#### Optional Enhancements

1. **Add a Range for Guesses**:
   - Allow the player to specify the range (e.g., 1–50 or 1–1000).

2. **Add Difficulty Levels**:
   - Easy: Unlimited guesses.
   - Medium: Maximum 10 guesses.
   - Hard: Maximum 5 guesses.

3. **Track High Scores**:
   - Save the fewest attempts in a file and display the high score.

4. **Play Again Option**:
   - Allow the player to play multiple rounds without restarting the program.
