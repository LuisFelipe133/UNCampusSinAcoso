from typing import Generic,TypeVar
from .DynamicArray import DynamicArray
T = TypeVar("T")

class Heap(Generic[T]): # DEFAULT MAX HEAP
    array:DynamicArray
    #************************************* constructor
    def __init__(self):
        self.array= DynamicArray()
    #************************************* verificacion y atributos
    def size(self):
        return self.array.index
    def getMax(self):
        return self.array.array[0]
    
    def maxSize(self):
        return self.array.size
    
    def parent(self,index):
        parent = int((index+1)/2)-1
        if parent >= self.size():
            raise Exception("Index not valid")
        else:
            return parent
            
    def leftChild(self,index):
        child= ((index + 1) * 2) - 1
        if child >= self.size():
            raise Exception("Index not valid ",child," and index",index)
        else:
            return child
        
    def rightChild(self,index):
        child= (((index + 1) * 2) + 1) - 1
        if child >= self.size():
            raise Exception("Index not valid: ",child,"and index ",index)
        else:
            return child

    #*************************************** Insertar, eliminar, etc
    def change_priority(self, index, nuevo):
        self.array.array[index] = nuevo
    
    def siftUp(self,index):
        parent = self.parent(index)
        if(index>0):
            if self.array.array[parent] < self.array.array[index]:
                aux = self.array.array[parent]
                self.array.array[parent] = self.array.array[index]
                self.array.array[index] = aux
                self.siftUp(parent)
    
    def insert(self,data:T):
        self.array.pushBack(data)
        self.siftUp(self.size()-1)
    
    def siftDown(self,index:int):
        maxIndex = index
        try:
            leftie = self.leftChild(index)
            if leftie<self.size() and self.array.array[leftie] > self.array.array[maxIndex]:
                maxIndex=leftie
        except:pass
        try:
            rightie = self.rightChild(index)
            if rightie<self.size() and self.array.array[rightie] > self.array.array[maxIndex]:
                maxIndex=rightie
        except:pass
        if index!=maxIndex:
            aux=self.array.array[index]
            self.array.array[index] = self.array.array[maxIndex]
            self.array.array[maxIndex] = aux
            self.siftDown(maxIndex)
    
    def insertUnordered(self,lista):
        self.array.array = None
        self.array.index =0
        self.array.array = lista
        self.array.index=len(lista)
        self.makeHeap()

    def remove(self, index):
        self.array.array[index] = self.getMax() + 1
        self.siftUp(index)
        self.extractMax()
    #************************************* Recorrer, imprimir, makeheap
    def extractMax(self):
        maxi = self.array.array[0]
        last = self.array.array[self.size() - 1]
        self.array.array[0] = last
        self.array.index -= 1
        self.siftDown(0)
        return maxi

    def makeHeap(self):
        order = self.parent(self.size() - 1)
        for i in range(order, -1, -1):
            self.siftDown(i)

    def heapSort(self):
        size = self.size()
        for i in range(size):
            data = self.extractMax()
            self.array.array[size - (i + 1)] = data
        self.array.index = size
        for i in range(int(size / 2)):
            aux = self.array.array[i]
            self.array.array[i] = self.array.array[size - (i + 1)]
            self.array.array[size - (i + 1)] = aux

    def printPreorderSubTree(self,index):
        if index >=self.size():
            return None
        print(self.array.array[index],end=" ")
        self.printPreorderSubTree(2*index + 1)  
        self.printPreorderSubTree( 2*index + 2)

    def printPreorder(self):
        self.printPreorderSubTree(0)
    
    def printPostOrderSubTree(self,index):
        if index >=self.size():
            return None
        self.printPostOrderSubTree(2*index + 1) 
        self.printPostOrderSubTree( 2*index + 2)
        print(self.array.array[index],end=" ") 
    def printPostOrder(self):
        self.printPostOrderSubTree(0)

    def printInOrderSubTree(self,index):
        if index >=self.size():
            return None
        self.printInOrderSubTree(2*index + 1)
        print(self.array.array[index],end=" ") 
        self.printInOrderSubTree( 2*index + 2)
    
    def printInOrder(self):
        self.printInOrderSubTree(0)
    
    def printArray(self):
        for i in range(0,self.array.index-1):
            print(self.array.array[i],end=" ")
