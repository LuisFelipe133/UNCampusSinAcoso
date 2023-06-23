
from typing import Generic, TypeVar
from .NodeList import NodeList
T = TypeVar("T")

class Queue():
    head:NodeList 
    tail:NodeList
    index:int
    
    #**************************** constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.index=0
    #**************************** metodos de verificación y atributos
    def isEmpty(self):
        return self.index==0
    def len(self):
        return self.index
     #**************************** Insertar o eliminar 
    def enqueue(self,data:T): #pushback
        dataNode = NodeList(data)
        if self.head==None:
            self.head = dataNode
            self.tail = dataNode
        else:
            self.tail.next = dataNode
            dataNode.prev = self.tail
            self.tail = dataNode
        self.index+=1
    def dequeue(self): #popfront
        temp:NodeList = self.head

        if self.head==None:
            temp = None
            raise Exception("No se puede eliminar en lista vacia")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        self.index-=1
        return temp.data
    
    
    #****************************************** buscar elementos
    def first(self): #topfront
        return self.head.data
    def last(self): #topback
        return self.tail.data
    
    def contains(self,data:T):
        if not self.isEmpty():
            ref = self.head
            while(ref!=None):
                if ref.data==data:
                    return True
                ref = ref.next
        return False
        
    def findPosition(self,data:T):
        if not self.isEmpty():
            ref = self.head
            pos = 0
            while(ref!=None):
                if ref.data==data:
                    self.position=pos
                    return pos
                ref = ref.next
                pos+=1
        return None
    
    def findNode(self,position:int):
        if position<=self.index and position>=0:
            ref:NodeList = self.head
            for i in range(0,position):
                ref = ref.next
            return ref.data
        else:
            raise Exception("Indice no está en la lista")
    
    def update(self,position:int,data:T):
        if position<=self.index and position>=0:
            ref:NodeList = self.head
            for i in range(0,position):
                ref = ref.next
            ref.data = data
        else:
            print("Indice no está en la lista")
    def peek(self):
        return self.head
    #**************************** Imprimir
    def printQueue(self):
        ref = self.head
        while(ref!=None):
            print(ref.data,end=" ")
            ref=ref.next
        print()