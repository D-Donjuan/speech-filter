from speechFilter import FileFilter

def showTitle():
    print("======================================================================")
    print("======================================================================")
    print("========================= Text File Filter ===========================")
    print("======================================================================")
    print("======================================================================\n")
    print("This program will get any text file and remove punctuations/common words")
    print("and count unique words in file. You will get the option to either remove")
    print("common words that are provided in a default file, which you can edit or")
    print("provide your own text file with your own common words to remove.\n")




def menuOptions():

    print("Please select one of the following options by entering the number associated with the choice")
    print("1. Edit/Enter wordStop File")
    print("2. Start Filtering Process")
    print("3. View Filtered TextFile History")
    print("4. Exit Program \n")

def optionChoice(userInstance):
    exitProgram = False

    while not exitProgram:

        menuOptions()
        choice = input("Please enter your choice: ")

        if choice == "1":
            editStopWordsFile(userInstance)
        elif choice == "2":
            initializeProgram(userInstance)
        elif choice == "3":
            userInstance.historyOfFilteredFiles()
        elif choice == "4":
            print("Thank you for using The File Filtering Program.")
            print("Good Bye!")
            exitProgram = True
        else:
            print("Invalid Option.")

def getTextFileName():
    
    fileNotChosen = True
    textFileName = ""

    while fileNotChosen:
        textFileName = input("Enter the file path and name for the text file you would like to use: ")
        print("Is this the correct file path and name you would like to use?: ", textFileName, "\n")
        choice = input("Type 'yes' to proceed or 'no' to retype file path and name: ")

        if choice == 'yes':
            fileNotChosen = False
        elif choice == 'no':
            print("Please re-enter the file path and name.")
        else:
            print("Invalid input")
    
    return textFileName

def selectStopWordFileOption():

    fileNotChosen = True
    stopWordFile = ''
    
    while fileNotChosen:

        print("Please choose an option for the StopWord File.")
        print("1. Use default StopWord File")
        print("2. Use your own StopWord File")
        stopWordFile = input("Enter your option: ")

        if stopWordFile == "1":
            stopWordFile = "stopWords.txt"
            fileNotChosen = False
        elif stopWordFile == "2":
            stopWordFile = getTextFileName()
            fileNotChosen = False
        else:
            print("Invalid Input")

    return stopWordFile

def editStopWordsFile(userInstance):

    notSelection = True
    while notSelection:
        print("Edit WordStop File Menu")
        print("1. View current words in stopWords file")
        print("2. Add stopWords to file")
        print("3. Remove stopWords to a file")
        print("4. Exit Edit Menu\n")
        selection = input("Please enter the number corresponding to the action above: ")

        if selection == "1":
            userInstance.testReadStopWordsFile()
        elif selection == "2":
            createAddWordsList(userInstance)
        elif selection == "3":
            createRemoveWordsList(userInstance)
        elif selection == "4":
            notSelection = False
        else:
            print("Invalid Option.")


def initializeProgram(userInstance):
    userInstance.removePunctuations()
    userInstance.removeStopWords()
    userInstance.countUniqueWords()
    print("\n")



def createRemoveWordsList(userInstance):
    
    finishInput = False
    deleteWordsList = []
    while not finishInput:
        deleteWord = input("Please enter the word you want to delete. Type :q to finish: ")
        if deleteWord == ":q":
            userInstance.removeStopWordsFromFile(deleteWordsList)
            finishInput = True
        else:
            deleteWordsList.append(deleteWord)
    print("\n")

    deleteWordsList = []

def createAddWordsList(userInstance):
    addWordsDone = False
    addWordsList = []

    while not addWordsDone:
        addWord = input("Please enter the word you want to add. Type :q to finish: ")
        if addWord == ":q":
            userInstance.addWordToFile(addWordsList)
            addWordsDone = True
        else:
            addWordsList.append(addWord)
    print("\n")
    addWordsList = []

    

