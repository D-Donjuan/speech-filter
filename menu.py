from speechFilter import FileFilter

def showTitle():
    print("======================================================================")
    print("======================================================================")
    print("========================= Text File Filter ===========================")
    print("======================================================================")
    print("======================================================================\n")
    print("This program will get any text file and remove punctuations/common words and count unique words in file. ")
    print("You will get the option to either remove common words that are provided in \n")
    print("a default file, which you can edit or provide your own text file with your own common words to remove.  \n")




def menuOptions():

    print("Please select one of the following options by entering the number associated with the choice")
    print("1. Start Filtering Process")
    print("2. Edit/Enter wordStop File")
    print("3. View Filtered TextFile History")
    print("5. Exit Program \n")

def optionChoice():
    exitProgram = False

    while not exitProgram:
        showTitle()
        menuOptions()
        choice = input("Please enter your choice: ")

        if choice == "1":
            initializeProgram()
        elif choice == "2":
            print("this is option 2")
        elif choice == "3":
            print("This is option 3")
        elif choice == "4":
            print("This is option 4")
        elif choice == "5":
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
        print("\n")
        print("Is this the correct file path and name you would like to use?: ", textFileName, "\n")

        choice = input("Type 'yes' to proceed or 'no' to retype file path and name: ")
        print("\n")

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
        print("2. Use your own StopWord File \n")
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


def initializeProgram():
    print("Please enter the text file that you would like to filter")
    fileTofilter = getTextFileName()
    stopWordFile = selectStopWordFileOption()

    debateFile = open(fileTofilter, "r")
    fileFilterString = debateFile.read()
    debateFile.close()


    stopWordsFile = open(stopWordFile, "r")
    stopWordsString = stopWordsFile.read()
    stopWordsFile.close()
    
    userInstance = FileFilter(fileFilterString, stopWordsString)
    userInstance.removePunctuations()
    userInstance.removeStopWords()
    userInstance.countUniqueWords()

    

