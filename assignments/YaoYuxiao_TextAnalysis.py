# Assignment 4: Text Analysis
# Read a text file and determine the word frequencies for those words
# in the vocabulary dictionary of computer terms
import string

# global variable for the dictionary created from computer_terms.txt
vocabulary_dictionary = {}


# Do not modify this function
def main():

    create_vocabulary_dictionary()
    calculate_word_frequencies()
    display_results()


# Read computer_terms.txt file.
# For each term, create an entry in the vocabulary_dictionary
# The term is the key, and the value will be the frequency of the term in the article file
def create_vocabulary_dictionary():
    global vocabulary_dictionary
    filename = 'computer_terms.txt'
    computer_terms = open(filename, 'r')

    # Fill the dictionary with the vocabulary(key) and frequency(value) association
    for vocabulary in computer_terms:
        vocabulary = vocabulary.strip()  # Remove whitespace like '\n'
        vocabulary_dictionary[vocabulary] = 0  # Initially, this value is 0.


# Read the article file, LearnToCode_LearnToThink.txt
# For each line in the file, call the normalize_text function.
# This function will return a list of normalized words for the line of text passed to it.
# For each word in the list, if it is in the vocabulary dictionary, increment its frequency in the dictionary
def calculate_word_frequencies():
    try:
        global vocabulary_dictionary
        filename = 'LearnToCode_LearnToThink.txt'
        article_file = open(filename, 'r').read()
        # Call the normalization function, a list of normalized words will be returned
        normalize_text(article_file)
        # Every word in the list should be tested if it is in the dictionary
        # If a word is defined in the dictionary, then increment its frequency
        for word in normalize_text(article_file):
            if word in vocabulary_dictionary:
                vocabulary_dictionary[word] = vocabulary_dictionary.get(word, 0)+1

    except FileNotFoundError as err:
        print('Error: cannot find the file')
        print('Error:', err)
    except OSError as err:
        print('Error: cannot access the file')
        print('Error:', err)
    except ValueError as err:
        print('Error: invalid data found in file')
        print('Error:', err)
    except Exception as err:  # catch all error handler, if the above handlers do not apply
        print('An unknown error occurred')
        print('Error:', err)


# See assignment slides for more information.
# Do NOT modify this function -- just call it, and use the list of words it returns.
# This function creates a list of normalized words from a line of text.
def normalize_text(line_of_text):
    normalized_words = []  # Initialize the list
    line_of_text = line_of_text.strip()  # Remove any leading or trailing whitespace
    list_of_words = line_of_text.split()  # Create a list of words from the line_of_text
    for word in list_of_words:
        normalized_word = word.strip(string.punctuation).lower()  # Remove punctuation and lowercase the word
        if normalized_word:  # this statement is True if normalized_word is NOT an empty string ('')
            normalized_words.append(normalized_word)
    return normalized_words


# Display the words from the article file that were found in the vocabulary_dictionary, along with their frequencies.
# See the 'expected output' in the assignment slides for correct results.
def display_results():
    print('WORD'.ljust(20), 'FREQUENCY')
    # Display the words in the dictionary that occur at least once in the article
    # Use '.ljust' to format, the length is 20
    for word in vocabulary_dictionary:
        if vocabulary_dictionary.get(word, 0) > 0:
            print(word.ljust(20), vocabulary_dictionary.get(word))


main()



