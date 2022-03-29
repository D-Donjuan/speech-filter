def showTitle():
    print("======================================================================")
    print("======================================================================")
    print("========================= Text File Filter ===========================")
    print("======================================================================")
    print("======================================================================\n")

def showProgramDescription():
    print("This program will get any text file and remove punctuations/common words and count unique words in file. ")
    print("You will get the option to either remove common words that are provided in \n")
    print("a default file, which you can edit or provide your own text file with your own common words to remove.  \n")

def fileChoose():
    showTitle()
    showProgramDescription()

    print("Please enter the file path of the file name that you would like to filter.")
    
    fileNotChosen = True
    filename = input("Enter the file path and name: ")

    while fileNotChosen:

        print("\n")
        print("is this the correct file path and name?: ", filename, "\n")

        choice = input("Type 'yes' to proceed or 'no' to retype file path and name: ")
        print("\n")

        if choice == 'yes':
            fileNotChosen = False
        elif choice == 'no':
            filename = input("Please re-enter the file path and name: ")
        else:
            filename = input("Invalid input. Please enter the file path and name: ")
    
    return filename


