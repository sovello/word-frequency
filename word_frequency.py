
from sys import *
from re import *
#from importiter import *
# read-in the file

def getFilePath():
    '''Reads the file and returns the contents of the file'''
    if len(argv) < 2 :
        return "Invalid"
    else:
        return argv[1]

# read in the file contents
def readFileContent( file_path ):
    '''return all lines in the file as list, if file not found, return None'''
    try:
        with open(file_path) as file_content:
            return file_content.readlines()
    except FileNotFoundError:
        return None



# - get common words from text
def getUnCommonWords(text_line):
    '''return all common and uncommon words found in the text. the basis for which a word
    is considered common is it should be less than 5 characters'''
    #common_words = []
    non_common_words = ''
    text = text_line.split()

    for word in text:
        if len(word) < 5:
            #common_words.extend(word)
            continue
        else:
            non_common_words = non_common_words+' '+word.lower()
    return non_common_words

# - remove all punctuations except - which is part of a word for some words
def stripOffSpecialChar(word):
    '''return a word with all special characters removed'''
    return sub(r'[^A-Za-z0-9\-]', '', word)

# get the frequency of words in the text
def getWordFrequency(text):
    '''returns a dictionary of words with the frequency of appearance in text'''
    text = text.split()
    word_frequencies = {}
    for word in text:
        word = stripOffSpecialChar(word)
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies

# sort the words in descending order of frequency
def sortDictionary(dictionary = {}, criteria = 'value', count=20, reverse=True):
    '''sort a dictionary based on criteria and
    return a sorted dictionary with count elements'''
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse)
    return sorted_dictionary[:count]

def drawHistogram(data = tuple(), scale=10):
    if scale < 10:
        factor = 10
    else:
        factor = scale
    for item, value in data:
        print("{}: {}".format(item, '#'*(value//factor)))
    print("Scale: 1:10")

# get the frequency of words in the text
def word_frequency(text):
    '''returns a dictionary of words with the frequency of appearance in text'''
    return getWordFrequency(text)


if __name__ == '__main__':
    file_path = getFilePath()
    if file_path == "Invalid":
        print("Usage: this_script_name absolute_file_path")
        exit()
    else:
        uncommon_words = ''
        file_content = readFileContent(file_path)
        if file_content is None:
            print("Make sure the file path is correct")
            exit()
        else:
            for text_line in file_content:
                uncommon_words = uncommon_words +' '+getUnCommonWords(text_line)

        word_frequency = getWordFrequency(uncommon_words)
        option = input("Should the output be sorted? Y/N ").lower()
        counts = input("How many elements do you want? ")

        if option == 'n':
            sorted_dictionary = sortDictionary(word_frequency, count=int(counts), reverse=False)
        else:
            sorted_dictionary = sortDictionary(word_frequency, count=int(counts), reverse=True)

        for word, frequency in sorted_dictionary:
            print("{} {}".format(word, frequency))
        print('-------------------------------------')
        drawHistogram(sorted_dictionary)
