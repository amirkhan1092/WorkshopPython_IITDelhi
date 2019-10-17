class ANDGate:
    def __init__(self, input1=0,input2=0):
        self.input1 = input1
        self.input2 = input2

    def printTruthTable(self):
        print("True table to be printed ")
        for i in range (2):
            for j in range (2) :
                self.printOutput(i, j)


    def getOutput(self, input1, input2):
        return input1 & input2

    def printOutput(self, input1, input2):
        return f'{input1} AND {input2} results {self.getOutput(input1, input2)}'
