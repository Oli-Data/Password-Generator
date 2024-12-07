import random

def lists():
    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", 
                    "{", "}", "[", "]", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/",
                    "\\", "|", "~", "`"]
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return num_list, symbols_list, char_list

def list_processing(char_list, symbols_list, num_list, char_limit, num_symbols, num_count):
    # Randomly grabs from the list using the amount the parameters the user wanted
    selected_characters = random.sample(char_list, char_limit)
    selected_symbols = random.sample(symbols_list, num_symbols)
    selected_numbers = random.sample(num_list, num_count)

    # Merges all the lists
    password_list = selected_characters + selected_symbols + selected_numbers

    # Once merged it shuffles characters in the list then makes a string
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    print("Oli Password Generator")
    print("Please provide the following parameters: ")

    # Inputs
    char_limit = int(input("How many characters long would you like your password to be? "))
    num_symbols = int(input("How many symbols would you like it to have? "))
    num_count = int(input("How many numbers would you like it to have? "))

    # Adjust character limit
    char_limit -= (num_symbols + num_count)
    if char_limit < 0:
        raise ValueError("Not enough characters to make a password.")

    # Get lists
    num_list, symbols_list, char_list = lists()

    # Generates password
    password = list_processing(char_list, symbols_list, num_list, char_limit, num_symbols, num_count)

    # Prints password
    print(f"Here is your password, please don't use it in more than one place: {password}")

if __name__ == "__main__":
    main()