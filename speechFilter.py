import string
import pprint


class FileFilter:


    def __init__(self, textFile, stopWordsFile):
        self.textFile = textFile
        self.stopWordsFile = stopWordsFile
        self.uniqueWords = {}
        self.history = {}

    def testReadTextFile(self):
        for i in self.textFile:
            print(i)

    def testReadStopWordsFile(self):
        for i in self.stopWordsFile:
            print(i)

    def removePunctuations(self):
        punctuations = string.punctuation

        for char in self.textFile:
            if char in punctuations:
                self.textFile = self.textFile.replace(char , "") 

    def removeStopWords(self):

        splitDebateText = self.textFile.split()
        splitStopWords = self.stopWordsFile.split()
        updatedDebateTextSplit = [word for word in splitDebateText if word.lower() not in splitStopWords]
        self.textFile = updatedDebateTextSplit

    def countUniqueWords(self):

        for word in self.textFile:
            if word in self.uniqueWords:
                self.uniqueWords[word] += 1
            else:
                self.uniqueWords[word] = 1
        
    def editStopWordsFile(self, input):
        stopWordFileSplit = self.stopWordsFile.split()
        updatedStopWordFile = [word for word in stopWordFileSplit if word.lower() not in input]
        self.stopWordsFile = ' '.join(updatedStopWordFile)
        # for x in self.stopWordsFile:
        #     print(x)

    def historyOfFilteredFiles(self):
        self.history["self.textFile"] = self.uniqueWords
        self.history["another.textFile"] = self.uniqueWords
        print(self.history)








        
        
