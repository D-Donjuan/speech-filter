from menu import optionChoice


def main():
    # debateFile = open("algo.txt", "r")
    # debateString = debateFile.read()
    # debateFile.close()


    # stopWordsFile = open("stopWords.txt", "r")
    # stopWordsString = stopWordsFile.read()
    # stopWordsFile.close()

    # firstInst = FileFilter(debateString, stopWordsString)
    # firstInst.removePunctuations()
    # firstInst.removeStopWords()
    # firstInst.countUniqueWords()
    # firstInst.historyOfFilteredFiles()
    # firstInst.testReadStopWordsFile()

    # finishInput = False
    # deleteWordsList = []

    # while not finishInput:
    #     deleteWord = input("Please enter the word you want to delete. Type :q to finish: ")
    #     if deleteWord == ":q":
    #         firstInst.removeStopWordsFromFile(deleteWordsList)
    #         finishInput = True
    #     else:
    #         deleteWordsList.append(deleteWord)

    # deleteWordsList = []

    # addWordsDone = False
    # addWordsList = []

    # while not addWordsDone:
    #     addWord = input("Please enter the word you want to add. Type :q to finish: ")
    #     if addWord == ":q":
    #         firstInst.addWordToFile(addWordsList)
    #         addWordsDone = True
    #     else:
    #         addWordsList.append(addWord)
        
    # addWordsList = []
        
    # firstInst.testReadStopWordsFile()

    optionChoice()


if __name__ == "__main__":
    main()