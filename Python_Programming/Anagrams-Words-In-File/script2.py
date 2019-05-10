'''
Function to get all the words from the file seperated by new line(\n).
'''
def getWordsFromFile(loc):
    with open(loc) as f:
        words = f.read().split('\n')
        words.pop() # delete the last . from the list of words
    return words
'''
Function to form a word by sorting a list of character in increasing order.
'''
def sortedWordList(char_list):
    word = ''.join([char for char in sorted(char_list)])
    # print(f'word:{word}')
    return word

'''
Function to create a list of words after sorting characters in increasing order.
'''
def sortedWords(word_list):
    sorted_words = []
    for word in word_list:
        sorted_words.append(sortedWordList(word))
    #print(f'sorted_words:{sorted_words}')
    return sorted_words

'''
    Function to create the dictionary with the words in the list
    as the key and a list of words which are its anagrams and are
    present in the file.
'''
def AnagramDictCreate(word_list, file_word_list):
    sorted_word_list = sortedWords(file_word_list)
    #print(f'sorted_word_list:{sorted_word_list}')
    anagram_dict = {}

    for word in word_list:
        sorted_word = sortedWordList(word)
        list_of_words = [file_word_list[index] for index,each_word in enumerate(
        sorted_word_list) if each_word == sorted_word]
        #print(list_of_words)
        anagram_dict[word] = list_of_words

    return anagram_dict

def main():

    # List of words in the given input
    word_list = ['radio','active', 'file','generation','waking', 'up', 'Hackerearth']

    file_word_list   = getWordsFromFile('tmp/dict/words.txt')
    anagram_dict = AnagramDictCreate(word_list, file_word_list)

    print (anagram_dict)

if __name__ == '__main__':
    main()
