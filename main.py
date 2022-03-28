from string import punctuation
from speechFilter import FileFilter
from menu import fileChoose
import string

def main():
    debateFile = open("debate.txt", "r")
    debateString = debateFile.read()
    debateFile.close()


    stopWordsFile = open("stopWords.txt", "r")
    stopWordsString = stopWordsFile.read()
    stopWordsFile.close()

    firstInst = FileFilter(debateString, stopWordsString)
    firstInst.removePunctuations()
    firstInst.removeStopWords()


if __name__ == "__main__":
    main()