# creates a clean list of unambiguous words
from LocalDir import *
import pickle

fileIn = "\\\\metaDictUnambiguousRaw.txt"
textOnlyOut = "\\\\metaDictUnambiguousWordsOnly.txt"
dirName = "D:\School\GSU\Skums\dictionary"
items = []
string = ""

with open(dirName + fileIn) as f:
    for line in f:
        for elem in line.split(';'):
            items.append(elem.strip())

items = sorted(set(items))
for item in items:
    print(item)
    string += item + "\n"

with open(dirName + textOnlyOut, "w") as f:
    f.write(string)

with open(unambiguousWordsListFile, "wb") as f:
    pickle.dump(items, f)