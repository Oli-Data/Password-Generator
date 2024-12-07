# Oli Password Generator

### Summary

This Python project demonstrates how to create a secure, customizable password generator. The program allows users to specify the total length of the password, the number of symbols, and the number of numbers included. Using Python’s built-in random module, the program generates a strong, randomized password that combines letters, symbols, and numbers based on the user’s preferences.

### Features

- Customizable Password Length: Users can define the total number of characters in the password.
- Symbol and Number Inclusion: Allows specifying the count of symbols and numbers to include in the password.
- Randomization: Shuffles the selected characters to ensure randomness and enhance security.

 ### Code Breakdown

1. Importing Required Module

The program imports the random module, which is essential for generating random samples and shuffling the password elements.

2. Defining Helper Functions

#### a. lists()

This function initializes and returns three lists:
- num_list: A list of numeric characters (0–9).
- symbols_list: A list of common symbols used in passwords.
- char_list: A list of lowercase alphabetic characters (a–z).

 #### b. list_processing()

This function processes the user’s input to generate a password:

1. Input Parameters:
- char_list, symbols_list, num_list: Lists containing the available characters.
- char_limit, num_symbols, num_count: User-defined counts for letters, symbols, and numbers.
 
2. Random Selection:
- Uses random.sample() to randomly select characters from the lists based on user specifications.
 
3. Merge and Shuffle:
- Combines all selected elements into a single list.
- Shuffles the combined list using random.shuffle() to enhance randomness.

4. Password Generation:
- Converts the shuffled list into a string using ''.join().

3. Main Function

#### The main() function serves as the program’s entry point:

1. User Input:
- Collects the desired total length of the password, the number of symbols, and the number of numbers.
- Validates that the sum of symbols and numbers does not exceed the total password length.
2. List Initialization:
- Calls the lists() function to retrieve character, symbol, and number lists.
3. Password Generation:
- Calls list_processing() to generate the password based on the user’s preferences.
4. Output:
- Prints the generated password.
