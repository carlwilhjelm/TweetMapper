import nltk

# nltk lematizer
import re
wnl = nltk.WordNetLemmatizer()
tok = nltk.word_tokenize

# make sure tweet processing is uniform
def tweetToTokens(tweetIn):
    # split and make lowercase
    # # lower() implemented in TweetMapper
    # tweetIn = tweetIn.lower()
    noWhite = tweetIn.split()
    goodWords = []
    # print(noWhite)
    for word in noWhite:
        if word == 'rt':
            continue
        elif word[0] == '#':
            goodWords.append(word[1:])
        elif word[0].isalpha() and word[0:4] != 'http':
            goodWords.append(word)
    # lemmatize
    lemmatizedWords = [wnl.lemmatize(w) for w in goodWords]
    # split on all non-alpha numeric chars
    charsOnly = re.split('[^a-zA-Z]', " ".join(lemmatizedWords))
    # remove empty strings
    cleanTokens = list(filter(None, charsOnly))
    # print(cleanTokens)
    return cleanTokens

