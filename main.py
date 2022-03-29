from string import punctuation
from speechFilter import FileFilter
from menu import fileChoose
import string

def main():
    debateFile = open("algo.txt", "r")
    debateString = debateFile.read()
    debateFile.close()


    stopWordsFile = open("stopWords.txt", "r")
    stopWordsString = stopWordsFile.read()
    stopWordsFile.close()

    firstInst = FileFilter(debateString, stopWordsString)
    firstInst.removePunctuations()
    firstInst.removeStopWords()
    firstInst.countUniqueWords()
    firstInst.historyOfFilteredFiles()
    firstInst.testReadStopWordsFile()
    finishInput = False
    deleteWordsList = []
    while not finishInput:
        deleteWord = input("Please enter the word you want to delete. Type :q to finish: ")
        if deleteWord == ":q":
            firstInst.editStopWordsFile(deleteWordsList)
            finishInput = True
        else:
            deleteWordsList.append(deleteWord)

    firstInst.testReadStopWordsFile()


if __name__ == "__main__":
    main()