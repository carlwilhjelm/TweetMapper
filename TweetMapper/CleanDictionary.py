# creates a clean list of unambiguous words
from LocalDir import *
import pickle

def mkList(textFile, listFile):
    with open(textFile, 'r') as f:
        items = f.read().split('\n')

    print(", ".join(items))
    with open(listFile, "wb") as f:
        pickle.dump(items, f)

mkList(allWordsTextFile, allWordsListFile)
mkList(unambiguousWordsTextFile, unambiguousWordsListFile)