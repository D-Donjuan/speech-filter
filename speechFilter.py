import string

class FileFilter:


    def __init__(self, textFile, stopWordsFile):
        self.textFile = textFile
        self.stopWordsFile = open(stopWordsFile, 'r')

    def testReadTextFile(self):
        for i in self.textFile:
            print(i)

    def testReadStopWordsFile(self):
        for i in self.stopWordsFile:
            print(i)

    def removePunctuations(self):
        text = self.textFile
        textSplitIntoWords = text.split(" ")
        puncCharacters = string.punctuation

        for char in text:
            if char in puncCharacters:
                text = t

        
        
