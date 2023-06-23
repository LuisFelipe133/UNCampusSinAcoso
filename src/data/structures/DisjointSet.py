from .DynamicArray import DynamicArray
class DisjointSet:
    setSize:int 
    parent:DynamicArray
    rank:DynamicArray
    def __init__(self,size:int):
        self.setSize=size
        self.parent = DynamicArray()
        self.rank = DynamicArray()
    
    def makeAllSet(self):
        for i in range(0,self.setSize):
            self.parent.array[i] = i
            self.parent.index=i+1
            self.rank.array[i]=0
            self.rank.index=i+1
    
    def makeOneSet(self,index):
        self.parent.array[index] = index
        self.rank.array[index]=0
    
    def find(self,element):
        if self.parent.array[element] != element:
            self.parent.array[element] = self.find(self.parent.array[element])
        return self.parent.array[element]

    def union(self,firstSet,secondSet):
        rootFirst = self.find(firstSet)
        rootSecond = self.find(secondSet)
        if rootFirst == rootSecond:
            return
        if self.rank.array[rootFirst] < self.rank.array[rootSecond]:
            self.parent.array[rootFirst] = rootSecond
        elif self.rank.array[rootFirst] > self.rank.array[rootSecond]:
            self.parent.array[rootSecond] = rootFirst
        else:
            self.parent.array[rootSecond] = rootFirst
            self.rank.array[rootFirst] += 1
            
    def isConnected(self, firstSet, secondSet):
        return self.find(firstSet) == self.find(secondSet)