from __future__ import unicode_literals
import string
import pprint


class FileFilter:


    def __init__(self, textFile, stopWordsFile, filename):
        self.textFile = textFile
        self.stopWordsFile = stopWordsFile
        self.filename = filename
        self.uniqueWords = {}
        self.history = {}

    def testReadTextFile(self):
        for i in self.textFile:
            print(i)

    def testReadStopWordsFile(self):
        listOfStopWords = self.stopWordsFile.split()
        for i in listOfStopWords:
            print(i)
        print("\n")

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
        
        self.uniqueWords = {}
        for word in self.textFile:
            if word in self.uniqueWords:
                self.uniqueWords[word] += 1
            else:
                self.uniqueWords[word] = 1
        
        print(self.uniqueWords)
        if self.filename in self.history:
            self.filename = self.filename + str(1)
        self.history[self.filename] = self.uniqueWords
        self.textFile = ' '.join(self.textFile)


        
    def removeStopWordsFromFile(self, input):
        stopWordFileSplit = self.stopWordsFile.split()
        updatedStopWordFile = [word for word in stopWordFileSplit if word.lower() not in input]
        self.stopWordsFile = ' '.join(updatedStopWordFile)


    def addWordToFile(self, input):
        stopWordFileSplit = self.stopWordsFile.split()
        for word in input:
            print(word)
            if word not in stopWordFileSplit:
                stopWordFileSplit.append(word)
            else:
                print(word, " is already in the stopWords textfile.")
        self.stopWordsFile = ' '.join(stopWordFileSplit)



    def historyOfFilteredFiles(self):
        print(self.history)








        
        
