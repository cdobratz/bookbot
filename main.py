import os
from collections import defaultdict

def main():
    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Specify the path to the file
    path_to_file = "/Users/myone/workspace/github.com/cdobratz/bookbot/.gitignore/books/frankenstein.txt"

    # Open the file and read its contents
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return

    # Count the number of words in the text
    word_count = count_words(file_contents)
    
    # Count the number of times each character appears in the text
    char_counts = num_char(file_contents)
    
    # Convert character counts dictionary to a list of dictionaries
    char_counts_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    
    # Sort the list by the number of occurrences in descending order
    char_counts_list.sort(key=lambda x: x["num"], reverse=True)
    
    # Print the report
    print(f"Number of words in 'frankenstein.txt': {word_count}")
    print("\nCharacter counts (sorted):")
    for item in char_counts_list:
        print(f"The {item['char']}: was found {item['num']} times")

def count_words(text):
    # Split the text into words using whitespace as delimiter
    words = text.split()
    # Return the number of words
    return len(words)

def num_char(text):
    # Convert the text to lowercase
    the_char = text.lower()
    
    # Initialize a defaultdict for counting characters
    char_count = defaultdict(int)
    
    # Count each character
    for char in the_char:
        char_count[char] += 1
    
    # Convert defaultdict to a regular dictionary and return
    return dict(char_count)

# Call the main function to execute the program
if __name__ == "__main__":
    main()