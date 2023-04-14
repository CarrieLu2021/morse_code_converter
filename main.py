# Import the Morse code dictionary from an external module
from morse_codes import morse_dict


def encode() -> str:
    """Convert the prompt message into Morse Codes.
    Letters separated by spaces and words by '/', unrecognized characters represented by '?'."""
    msg = input("Please type your messages to encode:\n").upper()
    morse_codes = ""
    for char in msg:
        if char == " ":
            code = "/ "
        elif char in morse_dict:
            code = morse_dict[char] + " "
        else:
            code = "?"
        morse_codes += code
    return morse_codes.strip()


def decode() -> str:
    """Convert prompt Morse Codes into a message. Unrecognized characters represented by '?'."""
    morse_words = input("Please type the Morse Codes you need to decode:\n").split(" ")
    msg = ""
    char = ''
    for morse_code in morse_words:
        if morse_code == "/":
            char = " "
        else:
            for key, value in morse_dict.items():
                if morse_code == value:
                    char = key
                    break
                else:
                    char = "?"
        msg += char
    return msg.upper()


print("Welcome to Morse Code Converter!⌨️")
game_on = True
while game_on:
    user_choice = input("Please type E for Encoding or D for Decoding: ").upper()

    if user_choice == "E":
        print(f"Here's your encoded message:\n{encode()}")
        game_on = False

    elif user_choice == "D":
        print(f"Here's your decoded message:\n{decode()}")
        game_on = False

    else:
        print("Invalid. Please try again.")

