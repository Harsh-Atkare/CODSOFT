# Password Generator #
## Overview ##
The Password Generator is a simple Python application with a graphical user interface (GUI) built using tkinter. This application allows users to generate strong, random passwords of specified lengths and copy them to the clipboard for easy use. The application leverages the secrets module to ensure that the generated passwords are cryptographically secure.

## Features ##

- User Input for Password Length: Users can specify the desired length of the password.
- Generate Secure Passwords: The application generates passwords using a combination of letters, digits, and punctuation characters.
- Copy to Clipboard: Users can easily copy the generated password to the clipboard with a click of a button.
- Graphical User Interface: Simple and user-friendly interface built with tkinter.

## Prerequisites ## 

- Python 3.x
- tkinter library (usually included with Python installations)
- pyperclip library for clipboard operations

## Installation ## 

1. Clone the repository:

     1.     git clone https://github.com/Harsh-Atkare/CODSOFT
     2.     cd CODSOFT/Python/Password_Generator

2. Install required dependencies:

        pip install pyperclip

## Usage ##

1. Run the application:

        python main.py

2. Specify the Password Length:

- Enter the desired length of the password in the input field.

3. Generate Password:

- Click the "Generate Password" button. The generated password will be displayed on the screen.

4. Copy Password:

- Click the "Copy Password" button to copy the generated password to the clipboard.
