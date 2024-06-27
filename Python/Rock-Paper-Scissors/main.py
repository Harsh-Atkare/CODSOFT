
import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        global user_score
        user_score += 1
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        return "Computer wins!"

# Function to handle the user's choice
def user_choice(choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"You chose {choice}, Computer chose {computer_choice}\n{result}")
    score_label.config(text=f"Score: You - {user_score} | Computer - {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text=f"Score: You - {user_score} | Computer - {computer_score}")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main interface
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18)).pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=20)

rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: user_choice('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: user_choice('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: user_choice('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="Make your choice!", font=("Helvetica", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score: You - {user_score} | Computer - {computer_score}", font=("Helvetica", 14))
score_label.pack(pady=20)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=20)

# Run the main loop
root.mainloop()
