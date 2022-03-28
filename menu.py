def showTitle():
    print("======================================================================")
    print("======================================================================")
    print("========================= Text File Filter ===========================")
    print("======================================================================")
    print("======================================================================\n")

def showProgramDescription():
    print("This program will remove common words/puncutations and only count words \n")
    print("That are unique. \n")

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
