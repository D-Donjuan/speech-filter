from speechFilter import FileFilter
from menu import showMenu

def main():
    textFile = showMenu()
    print(textFile)
    # firstInst = FileFilter("debate.txt", "stopWords.txt")
    # firstInst.removePunctuations()




if __name__ == "__main__":
    main()