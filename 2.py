def abbr(text):
    return ''.join(word[0].upper() for word in text.split() if word and word[0].isalpha())

phrase = "abc dfg gjk"
print(abbr(phrase))