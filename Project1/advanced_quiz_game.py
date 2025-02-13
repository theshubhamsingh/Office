import pandas as pd

def quiz_game_from_excel(file_path):
    try:
        # Load the Excel file
        data = pd.read_excel(file_path)
        
        print("Welcome to the Quiz Game!")
        print("Answer the following questions by typing the letter of your choice.\n")
        
        score = 0
        
        # Loop through each row in the Excel file
        for i, row in data.iterrows():
            print(f"Question {row['S.No']}: {row['Question']}")
            print(f"a) {row['Option A']}")
            print(f"b) {row['Option B']}")
            print(f"c) {row['Option C']}")
            print(f"d) {row['Option D']}")
            
            # Get the user's answer
            while True:
                answer = input("Your answer: ").strip().lower()
                if answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("Please choose only from the given options: a, b, c, or d.")
            
            # Check if the answer is correct
            if answer == row['Answer'].strip().lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was '{row['Answer']}'.\n")
        
        print(f"Your final score is: {score}/{len(data)}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "/Users/sam/Documents/Code/Python/Office/Project1/questions.xlsx"
    quiz_game_from_excel(file_path)
