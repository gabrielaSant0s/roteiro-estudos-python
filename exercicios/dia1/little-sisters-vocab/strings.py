def add_prefix_un(word):
    """
    :param word: str of a root word
    :return:  str of root word with un prefix
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return 'un'+word


def make_word_groups(vocab_words):
    """
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.
    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    string_vocab = vocab_words[0]

    for word in range(1,len(vocab_words)):
        string_vocab += f' :: {vocab_words[0]}{vocab_words[word]}' 
    
    return string_vocab


def remove_suffix_ness(word):
    """
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
    This function takes in a word and returns the base word with `ness` removed.
    """

    unsufix = word[:-4]

    if ( unsufix[-1] == 'i' ):
        return unsufix[:-1]+'y'
    else:
        return unsufix

def adjective_to_verb(sentence, index):
    """
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.
    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    split_sentence = sentence.split()
    new_word = split_sentence[index]+'en'

    if '.' in new_word:
        new_word = new_word.replace('.', '')

    return new_word

print(adjective_to_verb('It got dark as the sun set.', 2))
