# converts the words to piggy latin
def convert_word(word):
    from vowels import vowelfinder
    vowel = vowelfinder(word)
    first_letter = word[0]
    if first_letter in ["a", "e", "i", "o", "u"]:
        return word + "way"
    else:
        return word[vowel:] + word[:vowel] + "ay"


print(convert_word("google"))
print(convert_word("ggoogle"))


def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word)
        new_sentence = new_sentence + " "
    return new_sentence


print(convert_sentence("google is a good search engine"))
print(convert_sentence("ggoogle is not a search engine"))
