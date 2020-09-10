from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictionary = []
    with open(DICTIONARY, 'r') as f:
        list = f.readlines()                                                            # The following creates a list by reading each line of my .txt file.
        list = [i.strip('\n') for i in list]
    return list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for i in word.upper():
        letter = i
        print(letter)
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]
    return score



def max_word_value(maxword=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
