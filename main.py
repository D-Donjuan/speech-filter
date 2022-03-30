from menu import optionChoice, showTitle, getTextFileName, selectStopWordFileOption
from speechFilter import FileFilter


def main():

    showTitle()
    print("First we will need you to provide the text file you would like to filter")
    print("as well as the stopWords file if you choose to provide your own")
    fileToFilter = getTextFileName()
    stopWordsFile = selectStopWordFileOption()
    
    debateFile = open(fileToFilter, "r")
    fileFilterString = debateFile.read()
    debateFile.close()


    stopWordsFile = open(stopWordsFile, "r")
    stopWordsString = stopWordsFile.read()
    stopWordsFile.close()

    userInstance = FileFilter(fileFilterString, stopWordsString)
    optionChoice(userInstance)



if __name__ == "__main__":
    main()